from django.db import models
from users.models import User
from django.template.defaultfilters import slugify

class Suggestion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_moderated = models.BooleanField(default=False)  # Flag for moderation status
    is_denied = models.BooleanField(default=False)  # Flag for denial status
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to user if using authentication
    votes_for = models.IntegerField(default=0)
    votes_against = models.IntegerField(default=0)
    voters_for = models.ManyToManyField(User, related_name='for_suggestions', blank=True)
    voters_against = models.ManyToManyField(User, related_name='against_suggestions', blank=True)
    denial_reason = models.CharField(max_length=100, verbose_name= "Причина отказа", null=True, blank=True)

    def has_voted_for(self, user):
        return user in self.voters_for.all()
    
    def has_voted_against(self, user):
        return user in self.voters_against.all()
    
    def __str__(self):
        return self.title
    
