from typing import Any
from django.http import HttpResponse #нужна доля возврата html запросов
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import os

http_host = os.environ.get('HTTP_HOST')
def index(request):
    context: dict[str,Any]={ # нужна для передачи данных в .html шаблон
    'teachers':  ['Учитель', 'Классный руководитель', 'Школьная администрация'],
    'admin': ['Системный администратор'],
    'http_host': http_host,
    }
    return render(request, 'main/index.html', context) #возвращаем рендер .html файла в папке /templates(поиск тут по дефолту)/main/index.html; заполняем данные шаблона переменной 'context'

def teachers_list(request):
    return render(request, 'main/teachers_list.html') #возвращаем рендер .html файла в папке /templates(поиск тут по дефолту)/main/teachers_list.html;

def design_system (request):
    return render(request, 'main/design_system.html')

def rules_list(request):
    return render(request, 'main/rules.html')

def emergencies(request):
    return render(request, 'main/emergencies.html')