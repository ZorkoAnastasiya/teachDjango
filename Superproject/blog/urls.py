from django.urls import path
from blog import views


app_name = "blog"


urlpatterns = [
    path("", views.AllPostView.as_view(), name="home"),
    path("rubric/<int:rubric_id>/", views.RubricsPostView.as_view(), name="rubric"),
    path("<int:pk>/", views.SinglePostView.as_view(), name="single_post"),
    path("<int:pk>/update/", views.UpdatePostView.as_view(), name="update_post"),
    path("<int:pk>/delete/", views.DeletePostView.as_view(), name="delete_post"),
    path("add_post/", views.CreatePostView.as_view(), name= "create_post"),
]
