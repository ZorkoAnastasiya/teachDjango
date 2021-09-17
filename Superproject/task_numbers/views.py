import json
from json import JSONDecodeError
from typing import Union
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView

from task_numbers.models import Numbers


def get_data(
        name: str,
        number: int
) -> int:

    try:
        obj = Numbers.objects.get(name = name)
        obj.number += number
        obj.save()
        return obj.number
    except Numbers.DoesNotExist:
        obj = Numbers(name = name, number = number)
        obj.save()
        return obj.number


def parse_data(
        data: Union[str, int],
        user: str
) -> Union[int, None]:

    if isinstance(data, int):
        more, smaller = -100, 100
        if not (more <= data <= smaller):
            return
        message = get_data(user, data)
        return message
    else:
        if data != 'stop':
            return
        number = 0
        message = get_data(user, number)
        return message


@csrf_exempt
@require_http_methods(["POST"])
def handler(request: HttpRequest) -> HttpResponse:

    user = request.headers.get("X-USER")
    if not user:
        return HttpResponse("Пройдите авторизацию.", status = 403)

    try:
        data = json.loads(request.body)
        message = parse_data(data, user)
    except JSONDecodeError:
        return HttpResponse("Нет данных", status = 422)

    if message is None:
        return HttpResponse(
            "Разрешенный тип данных: целое число от -100 до 100 или слово stop.",
            status = 422
        )

    response = HttpResponse(message)
    response.headers["x-user"] = user
    return response


class ShowNumbersView(ListView):
    template_name = "task_numbers/hw.html"
    model = Numbers
