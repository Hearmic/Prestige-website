
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate, login, logout

from .models import User
from .forms import LoginUserForm,UserCreateForm
from rest_framework import viewsets
from .serializers import UserSerializer
import os 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer

def login_user(request):
    http_host = os.environ.get('HTTP_HOST')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = username
            request.session.save()  
            return redirect(f'http://{http_host}/main')
    else:
        form = LoginUserForm()
        return render(request, 'users/login.html', {'form': form})
    return render(request, 'users/try_again.html', {'form': form}) 

def logout_user(request):
    logout(request)
    return redirect ('users:login')# перенаправление на ссылку с именем "login" в облласти имен "users"


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