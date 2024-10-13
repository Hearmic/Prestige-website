"""
URL configuration for exit_notes project.

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
from exit_notes.app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.exit_notes_main, name='exit_notes'),
    path('how_it_works/',views.how_it_works, name='how_it_works'),
    path('<int:note_id>/', views.exit_notes_details, name='exit_notes_details'),
    path('<int:note_id>/parent_approve', views.parent_approve, name="parent_approve"),
    path('<int:note_id>/teacher_approve', views.teacher_approve, name="teacher_approve"),
    path('<int:note_id>/security_approve', views.security_approve, name="security_approve"),
    path("<int:note_id>/deny", views.deny, name="deny"),
    path('delete/<int:note_id>/', views.exit_notes_delete, name='delete'),
    path('qr_code/<int:note_id>/', views.generate_qr_code, name='generate_qr_code'),
]
