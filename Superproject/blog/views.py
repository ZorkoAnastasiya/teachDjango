from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post, Rubrics
from blog.forms import NewPostForm


class AllPostView(ListView):
    model = Post
    extra_context = {"title": "Home page", "header": "All Post"}

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


class UpdatePostView(UpdateView):
    model = Post
    form_class = NewPostForm


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
