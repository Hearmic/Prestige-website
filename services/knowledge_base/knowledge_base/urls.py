"""
URL configuration for knowledge_base project.

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
    path('', views.home, name='home'),
    path('material/<int:material_id>/', views.material_detail, name='material_detail'), # Страница учебного материала
    path('favorites/', views.favorite_materials, name='favorites'), # Страница избранных материалов
    path('material/add/', views.add_material, name='add_material'), # Страница добавления нового материала (для учителей/администраторов)
    path('material/<int:material_id>/edit/', views.edit_material, name='edit_material'),     # Страница редактирования материала (для учителей/администраторов)
    path('content/manage/', views.edit_material, name='edit_material'), # Страница управления контентом (для администраторов)
    path('statistics/', views.statistics_page, name='statistics'),   
]
