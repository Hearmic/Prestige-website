from django import forms
from django.forms import MultipleChoiceField
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.models import Group
# from django_select2 import Select2MultipleWidget, Select2Widget

class LoginUserForm(forms.Form):
    username = forms.CharField(label = 'Имя', max_length = 20,widget= forms.TextInput(attrs= {'class': 'form-input'}))
    password = forms.CharField(label = 'Пароль', widget = forms.PasswordInput(attrs= {'class': 'form-input'}))
 
 
class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','last_name','first_name', 'surname','password1', 'password2', 'parents']
        
    groups = MultipleChoiceField(
        choices=Group.objects.all().values_list('id', 'name')
    )
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['surname'].label = 'Отчество'
        self.fields['parents'].label = 'Родители'
        self.fields['head_teacher'].label = 'Классный руководитель'
        self.fields['groups'].label = 'Группы/Роли'