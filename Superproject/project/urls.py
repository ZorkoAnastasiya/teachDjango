from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path
from task_numbers.views import handler, ShowNumbersView


def hello_world(request: HttpRequest):
    return HttpResponse("Hello World")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("hw/", hello_world),
    path("task4/", handler),
    path("task4/info/", ShowNumbersView.as_view()),
]
