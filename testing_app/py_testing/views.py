from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

menu = ['Про сайт', 'Пройти тест', 'Зворотній звязок', 'Увійти']


def index(request):
    topic = Topic.objects.all()
    return render(request, 'py_testing/index.html', {'topic': topic,'menu': menu, 'title': 'Головна сторінка'})


def about(request):
    return render(request, 'py_testing/about.html', {'menu': menu, 'title': 'Про сайт'})


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h2>Архів по рокам</h2><p>{year}</p>")


def categories(request, catid):
    return HttpResponse(f"<h1>Сторінка категорій тестів по Python</h1> {catid}")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')
