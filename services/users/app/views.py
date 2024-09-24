
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login, logout

from .models import User
from .forms import LoginUserForm,UserCreateForm




def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid(): # проверка валидности формы
            cd=form.cleaned_data # получение данных из полей формы
            user = authenticate(request, username=cd['username'],password=cd['password'])   # проверка пользователя и пароля
            if user and user.is_active:    # проверка активности пользователя
                login(request, user)        # авторизация пользователя
                return HttpResponseRedirect(reverse('main:home'))  # перенаправление на ссылку с именем "home" в облласти имен "main"
    else:
        form = LoginUserForm()
        return render(request, 'users/try_again.html', {'form': form})
    return render(request, 'users/login.html', {'form': form}) 

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))# перенаправление на ссылку с именем "login" в облласти имен "users"


def register_user(request):
    User = get_user_model()  # Get the actual user model (custom or default)
    users = User.objects.all()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('users:register')
        else:
            context = {'form': form, 'users': users}
            return render(request, 'users/register.html', context)
    else:
        form = UserCreateForm()  # Create an empty form for initial rendering
        context = {'form': form, 'users': users}
        return render(request, 'users/register.html', context)