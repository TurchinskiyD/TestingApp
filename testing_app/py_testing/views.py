from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [{'title': 'Про сайт', 'url_name': 'about'},
        {'title': 'Пройти тест', 'url_name': 'runtest'},
        {'title': 'Зворотній звязок', 'url_name': 'contact'},
        {'title': 'Увійти', 'url_name': 'login'}
]


def index(request):
    topic = Topic.objects.all()
    question = Question.objects.all()
    context = {'topic': topic,
               'question': question,
               'menu': menu,
               'title': 'Головна сторінка',
               'cat_selected': 0,
               }

    return render(request, 'py_testing/index.html', context=context)


def about(request):
    return render(request, 'py_testing/about.html', {'menu': menu, 'title': 'Про сайт'})


def runtest(request):
    return HttpResponse(f'<h2>Пройти тест</h2>Сторінка в розробці')


def contact(request):
    return HttpResponse(f'<h2>Зворотній звязок</h2>Сторінка в розробці')


def login(request):
    return HttpResponse(f'<h2>Увійти</h2> Сторінка в розробці')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')


def show_question_info(request, ques_id):
    return HttpResponse(f'Інформація про {ques_id}')


def show_category(request, cat_id):
    question = Question.objects.filter(topic_id=cat_id)
    topic = Topic.objects.all()

    if len(question) == 0:
        raise Http404()

    context = {'topic': topic,
               'question': question,
               'menu': menu,
               'title': 'Відображення по категоріям',
               'cat_selected': cat_id,
               }

    return render(request, 'py_testing/index.html', context=context)




