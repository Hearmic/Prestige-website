from django.urls import path
from . import views  # Import views from current app

app_name = 'suggestions'  # Define app namespace for URL names

urlpatterns = [
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
