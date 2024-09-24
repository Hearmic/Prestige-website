from django import forms
from .models import StudyMaterial, Question, Answer

class AddStudyMaterialForm(forms.ModelForm):
        class Meta:
            model = StudyMaterial
            fields = ('__all__')
    
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']