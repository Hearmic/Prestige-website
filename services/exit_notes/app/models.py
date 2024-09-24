from django.db import models
from users.models import User
from django.urls import reverse

# Create your models here.
class exit_note(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    deactivate_on = models.DateTimeField()
    created_by = models.ForeignKey(User, related_name='exit_note_created_by', on_delete=models.CASCADE ,null=True, blank=True)
    parent_approved = models.ForeignKey(User, related_name='exit_note_parent_approved', on_delete=models.CASCADE ,null=True, blank=True)
    teacher_approved = models.ForeignKey(User, related_name='exit_note_teacher_approved', on_delete=models.CASCADE ,null=True, blank=True)
    security_approved = models.ForeignKey(User, related_name='exit_note_security_approved', on_delete=models.CASCADE ,null=True, blank=True)
    is_active=models.BooleanField( default = True)
    is_denied= models.BooleanField(default = False)
    denied_by = models.ForeignKey(User, related_name='exit_note_denied_by', on_delete=models.CASCADE ,null=True, blank=True)
    qr_code = models.ImageField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('exit_notes_details', args=[str(self.id)])