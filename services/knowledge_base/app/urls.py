from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('material/<int:material_id>/', views.material_detail, name='material_detail'), # Страница учебного материала
    path('favorites/', views.favorite_materials, name='favorites'), # Страница избранных материалов
    path('material/<str:subject_name>', views.subject_material, name='subject_material'),
    path('material/add/', views.add_material, name='add_material'), # Страница добавления нового материала (для учителей/администраторов)
    path('material/<int:material_id>/edit/', views.edit_material, name='edit_material'),     # Страница редактирования материала (для учителей/администраторов)
    path('content/manage/', views.edit_material, name='edit_material'), # Страница управления контентом (для администраторов)
    path('statistics/', views.statistics_page, name='statistics'),   # Страница статистики (для администраторов)
]