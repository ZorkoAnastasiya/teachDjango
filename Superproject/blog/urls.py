from django.urls import path
from blog.views import AllPostView, SinglePostView, get_rubrics, post_view, show_post, add_post

urlpatterns = [
    path("", post_view, name="home"),
    path("rubric/<int:rubric_id>/", get_rubrics, name="rubric"),
    path("<int:post_id>/", show_post, name="single_post"),
    path("add_post/", add_post, name="add_post"),
]
