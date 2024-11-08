
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    

class User(AbstractUser):
    surname = models.CharField(max_length=50, blank=True, null=True)
    parents = models.ManyToManyField('self', blank=True)
    sudy_group = models.IntegerField(default=1)
    grade = models.ForeignKey("app.Grade", on_delete=models.CASCADE, null=True, blank=True, related_name='grade')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='myuser_set', 
        blank=True,
        help_text='Группа к которой пренадлежит пользователь. Пользователь получит все права группы к которой пренадлежит',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='myuser_set',  
        blank=True,
        help_text='Отдельные права для конкретногот пользователя (не используются)',
    )
    objects = UserManager

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    def __str__(self):
        return f"{self.last_name} {self.first_name}  {self.surname}"
    

class Grade(models.Model):
    grade_number = models.IntegerField()  # Класс (например, "6")
    litera = models.CharField(max_length=1)  # Буква литеры (например, "А")
    head_teacher = models.ForeignKey(User, related_name="teacher" , on_delete=models.CASCADE) # Классный руководитель (Пользователь)
    students = models.ManyToManyField(User, related_name="student") # Ученики (Пользователи)
    parents = models.ManyToManyField(User, related_name="parent") # Родители  (Пользователи)
    def __str__(self):
        return f'{self.grade_number}"{self.litera}"класс' #Оглавление записи (например 6"А"класс)

