from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('',views.display_menu, name= 'menu_display'),
    path('menu_list/', views.display_menu_list, name="menu_list"),
    path('dishes/', views.dish_list, name= 'dishes_list'), 
    path('create/dish/', views.create_dish, name='create_dish'),
    path('create/drink/', views.create_drink, name='create_drink'),
    path('meal_sets/', views.MealSet_list, name='meal_sets'),
    path('meal_sets/create/', views.create_set, name='create_set'),
    path('meal_sets/create/breakfast/', views.create_breakfast_set, name='create_breakfast_set'),
    path('meal_sets/create/lunch/', views.create_lunch_set, name='create_lunch_set'),
    path('meal_sets/create/dinner/', views.create_dinner_set, name='create_dinner_set'),
    path('meal_sets/update/breakfast/', views.update_breakfast_MealSet, name='update_breakfast_set'),
    path('meal_sets/update/lunch/', views.update_lunch_MealSet, name='update_lunch_set'),
    path('meal_sets/update/dinner/', views.update_dinner_MealSet, name='update_dinner_set'),
    path('allergies/', views.create_allergies, name='allergies_list'),
    path('allergies/delete/<int:allergies_id>', views.delete_allergies, name='delete_allergie'),
]
