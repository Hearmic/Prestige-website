"""
URL configuration for suggestions project.

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
    path('admin/', admin.site.urls),
    path('create/', views.create_suggestion, name='create_suggestion'),
    path('', views.suggestion_list, name='suggestion_list'),
    path('unmoderated/', views.unmoderated_suggestion_list, name='unmoderated_suggestion_list'),
    path('moderate/<int:suggestion_id>', views.moderate_suggestion, name='moderate_suggestion'),
    path('delete/<int:suggestion_id>', views.delete_suggestion, name='delete_suggestion'),
    path('vote_for/<int:suggestion_id>', views.vote_for, name='vote_for'),
    path('vote_against/<int:suggestion_id>', views.vote_against, name='vote_against'),
    path('suggestion/<int:suggestion_id>', views.suggestion_detail, name='suggestion_detail'),
    path('my_suggestions/', views.my_suggestions, name='my_suggestions'),
    path('deny/<int:suggestion_id>', views.deny_suggestion, name='deny_suggestion'),
]
