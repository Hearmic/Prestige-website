"""
URL configuration for schedules project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('schedules/admin/', admin.site.urls),
    path('schedules/', views.main, name='main'),
    path('schedules/schedule/<int:grade>/<str:litera>/', views.schedule_detail, name='schedule_detail'),
    path('schedules/create_schedule/', views.create_schedule, name='create_schedule'),
    path('schedules/create_lesson/',views.create_lesson, name='create_lesson'),
    path('schedules/lesson_details/<int:lesson_id>/', views.lesson_details, name='lesson_details'),
]
