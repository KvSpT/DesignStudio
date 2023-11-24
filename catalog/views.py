from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UserForm
from .models import Project, User
from django.shortcuts import redirect

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
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')

        user = authenticate(request, username=login, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли!')
            return redirect('account')
        else:
            messages.error(request, 'Неверный логин или пароль.')

    return render(request, 'login.html')
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from django.views import generic
class registration(generic.CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')

    # def post(self, request):
    #     form = self.form_class(request.POST)
    #
    #     if form.is_valid():  # проверяем форму регистрации
    #         user = form.save(commit=False)
    #         user.first_name = form.cleaned_data['first_name']
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user.set_password(password)
    #         user.save()
    #
    #         user = authenticate(username=username, password=password)
    #
    #         if user is not None and user.is_active:
    #             login(request, user)
    #             return HttpResponseRedirect("/")
    #
    #     return render(request, self.template_name, locals())

@login_required
def account(request):
    # Получаем текущего пользователя
    user = request.user

    # Получаем заявки текущего пользователя
    user_requests = user.requests.all()

    context = {
        'user': user,
        'user_requests': user_requests,
    }

    return render(request, 'account.html', context)

