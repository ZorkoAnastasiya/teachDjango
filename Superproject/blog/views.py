from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from blog.models import Post, Rubrics
from blog.forms import NewPostForm, UserRegisterForm, UserLoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class AllPostView(ListView):
    model = Post
    extra_context = {
        "title": "Home page",
        "header": "All Post"
    }
    paginate_by = 4

    def get_queryset(self):
        return self.model.objects.filter(
            hidden=False
        ).select_related('rubric')


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
        return self.model.objects.filter(hidden=False)


class CreatePostView(LoginRequiredMixin, CreateView):
    form_class = NewPostForm
    template_name = "blog/post_form.html"
    extra_context = {
        "title": "Adding a new post",
        "header": "Adding a new post"
    }
    login_url = "blog:login"


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = NewPostForm
    extra_context = {
        "title": "Post Update",
        "header": "Post Update"
    }
    login_url = "blog:login"


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')
    login_url = "blog:login"


def register(request: HttpRequest):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('blog:home')
        else:
            messages.error(request, "Registration error")
    else:
        form = UserRegisterForm()
    return render(request, "blog/register.html", {"form": form})


def user_login(request: HttpRequest):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("blog:home")
    else:
        form = UserLoginForm()
    return render(request, "blog/login.html", {"form": form})


def user_logout(request: HttpRequest):
    logout(request)
    return redirect("blog:login")
