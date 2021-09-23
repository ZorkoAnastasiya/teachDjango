from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from blog.models import Post, Rubrics
from blog.forms import NewPostForm


class AllPostView(ListView):
    model = Post


class SinglePostView(DetailView):
    model = Post


def post_view(request):
    header = "Home page"
    posts = Post.objects.all()
    context = {
        "header": header,
        "posts": posts,
    }
    return render(request, template_name = "blog/post_list.html", context = context)


def get_rubrics(request, rubric_id):
    posts = Post.objects.filter(rubric_id=rubric_id)
    rubric = Rubrics.objects.get(pk=rubric_id)
    return render(request, "blog/rubrics.html", {"posts": posts, "rubric": rubric})


def show_post(request: HttpRequest, post_id: int):
    post_item = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/post_detail.html", {"post_item": post_item})


def add_post(request: HttpRequest):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = NewPostForm()
    return render(request, "blog/add_post.html", {"form": form})
