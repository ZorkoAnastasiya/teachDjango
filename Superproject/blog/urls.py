from django.urls import path
from blog import views
from django.contrib.auth.views import LogoutView


app_name = "blog"


urlpatterns = [
    path("", views.AllPostView.as_view(), name="home"),
    path("mypost/", views.AllMyPostView.as_view(), name= "all_my_post"),
    path("rubric/<int:rubric_id>/", views.RubricsPostView.as_view(), name="rubric"),
    path("<int:pk>/", views.SinglePostView.as_view(), name="single_post"),
    path("<int:pk>/update/", views.UpdatePostView.as_view(), name="update_post"),
    path("<int:pk>/delete/", views.DeletePostView.as_view(), name="delete_post"),
    path("add_post/", views.CreatePostView.as_view(), name= "create_post"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name= "login"),
    path("logout/", LogoutView.as_view(), name= "logout"),
]
