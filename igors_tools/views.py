from django.http import HttpRequest
from django.shortcuts import render


def puny(request):
    text_to_convert = request.GET.get('text')
    if text_to_convert is not None:
        text_to_convert = text_to_convert.encode('idna')
        text_to_convert = text_to_convert.decode('utf8')
    else:
        text_to_convert = ""

    return render(request, "igors_tools/puny.html", {"text_to_convert": text_to_convert})


def tg_messager(request):
    return render(request, "igors_tools/my_css/tg_messager.html")


def person(request):
    return render(request, "igors_tools/my_css/persona.html")
