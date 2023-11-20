from django.shortcuts import render
from .models import Project, User

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_working_projects=Project.objects.filter(status__exact='w').count()
    new_projects=Project.objects.filter(status__exact='n')


    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_working_projects':num_working_projects,'new_projects':new_projects},
    )
