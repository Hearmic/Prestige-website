from django.db import models
from users.models import User, Grade


# Модель для категорий (предметов)
class Subject(models.Model):
    name = models.CharField(max_length=200)  # Название предмета (например, "Математика")
    description = models.TextField(null=True, blank=True)  # Описание предмета (опционально)

    def __str__(self):
        return self.name


# Модель для типов материалов (презентация, тест и т.д.)
class MaterialType(models.Model):
    name = models.CharField(max_length=100)  # Тип материала (например, "Презентация", "Тест")

    def __str__(self):
        return self.name

# Модель для учебных материалов
class StudyMaterial(models.Model):
    title = models.CharField(max_length=255)  # Название материала
    description = models.TextField(null=True, blank=True)  # Описание материала
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='materials')  # Предмет
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='materials')  # Класс
    material_type = models.ForeignKey(MaterialType, on_delete=models.SET_NULL, null=True)  # Тип материала
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор (учитель или администратор)
    upload_date = models.DateTimeField(auto_now_add=True)  # Дата загрузки
    files = models.FileField(upload_to='materials/files/', null=True, blank=True)  # Файл материала
    link = models.URLField(null=True, blank=True)  # Внешняя ссылка на материал (опционально)
    views = models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-upload_date']  # Сортировка по дате загрузки (по убыванию)

# Модель для избранного
class FavoriteMaterial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь
    material = models.ForeignKey(StudyMaterial, on_delete=models.CASCADE, related_name='favorites')  # Учебный материал
    added_at = models.DateTimeField(auto_now_add=True)  # Дата добавления в избранное

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.user.surname} добавил {self.material.title} в избранное"
    

class Question(models.Model):
    material = models.ForeignKey(StudyMaterial, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)

    def __str__(self): 
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text