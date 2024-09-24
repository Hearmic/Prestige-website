from django import forms
from .models import exit_note

class ExitNoteForm(forms.ModelForm):
    class Meta:
        model = exit_note
        fields = ['title', 'description']
    
