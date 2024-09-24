from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('',views.index, name='home'),
    path('teachers/',views.teachers_list, name='teachers_list'),
    path('rules/',views.rules_list, name='rules'),
    path('emergency_plots/', views.emergencies, name='emergencies'),
    path('design/',views.design_system, name='design_system'),
]
