import os
from django.http import HttpRequest, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from task_numbers.models import Numbers


def get_number(name):
    try:
        obj = Numbers.objects.get(name=name)
        number = obj.number
        return number
    except Numbers.DoesNotExist:
        obj = Numbers(name=name, number=0)
        obj.save()
        number = 0
        return number


def add_number(name, number):
    try:
        obj = Numbers.objects.get(name=name)
        number = obj.number + int(number)
        obj.number = number
        obj.save()
        return number
    except Numbers.DoesNotExist:
        obj = Numbers(name=name, number=number)
        obj.save()
        return number


@csrf_exempt
def handler(request: HttpRequest) -> HttpResponse:

    if request.method != "POST":
        return HttpResponse(status = 405)

    user = request.COOKIES.get("user")
    if user is None:
        user = os.urandom(16).hex()

    try:
        text = request.body.decode()
    except MultiValueDictKeyError:
        text = ''

    if text == "stop":
        message = get_number(user)
    elif text.isdigit():
        message = add_number(user, text)
    else:
        message = "Нет данных!"

    response = HttpResponse(f"Твое текущее число: {message}")
    response.set_cookie("user", user)
    return response
