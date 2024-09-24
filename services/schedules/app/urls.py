from django.urls import path

from . import views

app_name = 'schedules'

urlpatterns = [
    path('', views.main, name='main'),
    path('schedule/<int:grade>/<str:litera>/', views.schedule_detail, name='schedule_detail'),
    path('create_schedule/', views.create_schedule, name='create_schedule'),
    path('create_lesson/',views.create_lesson, name='create_lesson'),
    path('lesson_details/<int:lesson_id>/', views.lesson_details, name='lesson_details'),
]