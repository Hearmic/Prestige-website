from django import forms
from .models import Suggestion

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['title', 'description']
        


class DenialReasonForm(forms.Form):
    denial_reason = forms.CharField(widget=forms.Textarea, label='Причина отказа', max_length=100)
