from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post, Rubrics
from blog.forms import NewPostForm


class AllPostView(ListView):
    model = Post
    extra_context = {"title": "Home page", "header": "All Post"}

    def get_queryset(self):
        return Post.objects.filter(hidden=False)


class RubricsPostView(ListView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Rubrics.objects.get(pk=self.kwargs['rubric_id'])
        context['header'] = Rubrics.objects.get(pk=self.kwargs['rubric_id'])
        return context

    def get_queryset(self):
        return Post.objects.filter(rubric_id=self.kwargs['rubric_id'], hidden=False)


class SinglePostView(DetailView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(hidden=False)


class CreatePost(CreateView):
    form_class = NewPostForm
    template_name = "blog/add_post.html"


