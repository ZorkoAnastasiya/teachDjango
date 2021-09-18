from django.urls import path
from task_numbers.views import handler, ShowNumbersView

urlpatterns = [
    path("", handler),
    path("info/", ShowNumbersView.as_view()),
]
