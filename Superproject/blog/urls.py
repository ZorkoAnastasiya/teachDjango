from django.urls import path
from blog.views import AllPostView, SinglePostView, RubricsPostView, CreatePost

urlpatterns = [
    path("", AllPostView.as_view(), name="home"),
    path("rubric/<int:rubric_id>/", RubricsPostView.as_view(), name="rubric"),
    path("<int:pk>/", SinglePostView.as_view(), name="single_post"),
    path("add_post/", CreatePost.as_view(), name="add_post"),
]
