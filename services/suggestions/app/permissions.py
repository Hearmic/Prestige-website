from django.contrib.auth.models import Permission

class CanDeleteSuggestion(Permission):
    name = 'Can delete suggestion'