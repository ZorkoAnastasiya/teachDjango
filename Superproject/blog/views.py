from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from blog.models import Post, Rubrics
from blog.forms import NewPostForm


class AllPostView(ListView):
    model = Post
    extra_context = {
        "title": "Home page",
        "header": "All Post"
    }

    def get_queryset(self):
        return self.model.objects.filter(hidden=False)


class RubricsPostView(ListView):
    model = Post

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
        )


class SinglePostView(DetailView):
    model = Post

    def get_queryset(self):
        return self.model.objects.filter(hidden=False)


class CreatePostView(CreateView):
    form_class = NewPostForm
    template_name = "blog/post_form.html"
    extra_context = {
        "title": "Adding a new post",
        "header": "Adding a new post"
    }


class UpdatePostView(UpdateView):
    model = Post
    form_class = NewPostForm
    extra_context = {
        "title": "Post Update",
        "header": "Post Update"
    }


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')
