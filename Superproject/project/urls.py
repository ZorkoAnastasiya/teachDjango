from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path, include


def hello_world(request: HttpRequest):
    return HttpResponse("Hello World")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("hw/", hello_world),
    path("task4/", include("task_numbers.urls")),
]
