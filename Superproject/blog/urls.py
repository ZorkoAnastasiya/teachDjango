from django.urls import path
from blog.views import AllPostView, SinglePostView


urlpatterns = [
    path("", AllPostView.as_view()),
    path("<int:pk>/", SinglePostView.as_view())
]
