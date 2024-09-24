from django.apps import AppConfig


class SuggestionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suggestions'
    verbose_name = 'Предложения'  # Assuming this is the verbose name for your app in Russian