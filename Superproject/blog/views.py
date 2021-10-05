from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView
from django.views.generic import DeleteView, FormView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post, Rubrics
from blog.forms import NewPostForm, UserRegisterForm, UserLoginForm


class AllPostView(ListView):
    model = Post
    extra_context = {
        "title": "Home page",
        "header": "All Posts"
    }
    paginate_by = 4

    def get_queryset(self):
        return self.model.objects.filter(
            hidden=False
        ).select_related('rubric')


class AllMyPostView(ListView):
    model = Post
    extra_context = {
        "title": "My Post",
        "header": "My Post"
    }
    paginate_by = 2

    def get_queryset(self):
        author = self.request.user
        return super().get_queryset().filter(author=author)


class RubricsPostView(ListView):
    model = Post
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        rubric_id = Rubrics.objects.get(pk=self.kwargs['rubric_id'])
        context['title'] = rubric_id
        context['header'] = rubric_id
        return context

    def get_queryset(self):
        return self.model.objects.filter(
            rubric_id=self.kwargs['rubric_id'],
            hidden=False
        ).select_related('rubric')


class SinglePostView(DetailView):
    model = Post

    def get_queryset(self):
        return super().get_queryset().filter(hidden=False)


class CreatePostView(LoginRequiredMixin, CreateView):
    form_class = NewPostForm
    template_name = "blog/post_form.html"
    extra_context = {
        "title": "Adding a new post",
        "header": "Adding a new post"
    }
    login_url = "blog:login"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = NewPostForm
    extra_context = {
        "title": "Post Update",
        "header": "Post Update"
    }
    login_url = "blog:login"

    def get_queryset(self):
        author = self.request.user
        return super().get_queryset().filter(author=author)


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')
    login_url = "blog:login"

    def get_queryset(self):
        author = self.request.user
        return super().get_queryset().filter(author=author)


class UserRegisterView(SuccessMessageMixin, FormView):
    form_class = UserRegisterForm
    template_name = "blog/register.html"
    success_message = 'You have successfully registered!'
    success_url = reverse_lazy("blog:home")

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        message = messages.error(self.request, "Registration error")
        return self.render_to_response(self.get_context_data(form = form, message=message))


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "blog/login.html"
