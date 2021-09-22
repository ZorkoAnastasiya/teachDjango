from django.views.generic import ListView, DetailView
from blog.models import Post


class AllPostView(ListView):
    model = Post


class SinglePostView(DetailView):
    model = Post



