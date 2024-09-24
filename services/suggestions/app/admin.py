from django.contrib import admin
from django.contrib.auth.models import Group
from suggestions.models import Suggestion

admin.site.register(Suggestion)
