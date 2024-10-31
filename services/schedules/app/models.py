from django.db import models
from .user_api import get_user_by_id

def get_lesson_info(lesson):
    try:
        user_data = get_user_by_id(lesson.teacher_id)
        first_name = user_data['first_name']
        surname = user_data['surname']
        return f"{lesson.lesson_type} {first_name} {surname}"
    except (KeyError, TypeError):
        # Handle errors if user data is missing or invalid
        return f"{lesson.lesson_type} (Teacher information not found)"
    
class Lessons(models.Model):
    lesson_type = models.CharField(max_length=20)
    teacher_id = models.IntegerField()
    classroom = models.CharField(max_length=20)
    taught_from = models.IntegerField(default=1)

    def __str__(self):
        return get_lesson_info(self)

class school_schedule (models.Model):
    grade = models.IntegerField()
    litera = models.CharField(max_length=1)
    group = models.IntegerField(default=1)
    # Понедельник
    monday_lesson1 = models.ForeignKey(Lessons, related_name='monday_lesson1',null=True, blank=True, on_delete = models.CASCADE)
    monday_lesson2 = models.ForeignKey(Lessons, related_name='monday_lesson2',null=True, blank=True, on_delete = models.CASCADE)
    monday_lesson3 = models.ForeignKey(Lessons, related_name='monday_lesson3',null=True, blank=True, on_delete = models.CASCADE)
    monday_lesson4 = models.ForeignKey(Lessons, related_name='monday_lesson4',null=True, blank=True, on_delete = models.CASCADE)
    monday_lesson5 = models.ForeignKey(Lessons, related_name='monday_lesson5',null=True, blank=True, on_delete = models.CASCADE)
    monday_lesson6 = models.ForeignKey(Lessons, related_name='monday_lesson6',null=True, blank=True, on_delete = models.CASCADE)
    monday_lesson7 = models.ForeignKey(Lessons, related_name='monday_lesson7',null=True, blank=True, on_delete = models.CASCADE)
    monday_lesson8 = models.ForeignKey(Lessons, related_name='monday_lesson8',null=True, blank=True, on_delete = models.CASCADE)
    monday_lesson9 = models.ForeignKey(Lessons, related_name='monday_lesson9',null=True, blank=True, on_delete = models.CASCADE)
    # Вторник
    tuesday_lesson1 = models.ForeignKey(Lessons, related_name='tuesday_lesson1',null=True, blank=True, on_delete = models.CASCADE)
    tuesday_lesson2 = models.ForeignKey(Lessons, related_name='tuesday_lesson2',null=True, blank=True, on_delete = models.CASCADE)
    tuesday_lesson3 = models.ForeignKey(Lessons, related_name='tuesday_lesson3',null=True, blank=True, on_delete = models.CASCADE)
    tuesday_lesson4 = models.ForeignKey(Lessons, related_name='tuesday_lesson4',null=True, blank=True, on_delete = models.CASCADE)
    tuesday_lesson5 = models.ForeignKey(Lessons, related_name='tuesday_lesson5',null=True, blank=True, on_delete = models.CASCADE)
    tuesday_lesson6 = models.ForeignKey(Lessons, related_name='tuesday_lesson6',null=True, blank=True, on_delete = models.CASCADE)
    tuesday_lesson7 = models.ForeignKey(Lessons, related_name='tuesday_lesson7',null=True, blank=True, on_delete = models.CASCADE)
    tuesday_lesson8= models.ForeignKey(Lessons, related_name='tuesday_lesson8',null=True, blank=True, on_delete = models.CASCADE)
    tuesday_lesson9 = models.ForeignKey(Lessons, related_name='tuesday_lesson9',null=True, blank=True, on_delete = models.CASCADE)
    #Среда
    wednesday_lesson1 = models.ForeignKey(Lessons, related_name='wednesday_lesson1',null=True, blank=True, on_delete = models.CASCADE)
    wednesday_lesson2 = models.ForeignKey(Lessons, related_name='wednesday_lesson2',null=True, blank=True, on_delete = models.CASCADE)
    wednesday_lesson3 = models.ForeignKey(Lessons, related_name='wednesday_lesson3',null=True, blank=True, on_delete = models.CASCADE)
    wednesday_lesson4 = models.ForeignKey(Lessons, related_name='wednesday_lesson4',null=True, blank=True, on_delete = models.CASCADE)
    wednesday_lesson5 = models.ForeignKey(Lessons, related_name='wednesday_lesson5',null=True, blank=True, on_delete = models.CASCADE)
    wednesday_lesson6 = models.ForeignKey(Lessons, related_name='wednesday_lesson6',null=True, blank=True, on_delete = models.CASCADE)
    wednesday_lesson7 = models.ForeignKey(Lessons, related_name='wednesday_lesson7',null=True, blank=True, on_delete = models.CASCADE)
    wednesday_lesson8 = models.ForeignKey(Lessons, related_name='wednesday_lesson8',null=True, blank=True, on_delete = models.CASCADE)
    wednesday_lesson9 = models.ForeignKey(Lessons, related_name='wednesday_lesson9',null=True, blank=True, on_delete = models.CASCADE)
    #Четверг
    thursday_lesson1 = models.ForeignKey(Lessons, related_name='thursday_lesson1',null=True, blank=True, on_delete = models.CASCADE)
    thursday_lesson2 = models.ForeignKey(Lessons, related_name='thursday_lesson2',null=True, blank=True, on_delete = models.CASCADE)
    thursday_lesson3 = models.ForeignKey(Lessons, related_name='thursday_lesson3',null=True, blank=True, on_delete = models.CASCADE)
    thursday_lesson4 = models.ForeignKey(Lessons, related_name='thursday_lesson4',null=True, blank=True, on_delete = models.CASCADE)
    thursday_lesson5 = models.ForeignKey(Lessons, related_name='thursday_lesson5',null=True, blank=True, on_delete = models.CASCADE)
    thursday_lesson6 = models.ForeignKey(Lessons, related_name='thursday_lesson6',null=True, blank=True, on_delete = models.CASCADE)
    thursday_lesson7 = models.ForeignKey(Lessons, related_name='thursday_lesson7',null=True, blank=True, on_delete = models.CASCADE)
    thursday_lesson8 = models.ForeignKey(Lessons, related_name='thursday_lesson8',null=True, blank=True, on_delete = models.CASCADE)
    thursday_lesson9 = models.ForeignKey(Lessons, related_name='thursday_lesson9',null=True, blank=True, on_delete = models.CASCADE)
    #Пятница
    friday_lesson1 = models.ForeignKey(Lessons, related_name='friday_lesson1',null=True, blank=True, on_delete = models.CASCADE)
    friday_lesson2 = models.ForeignKey(Lessons, related_name='friday_lesson2',null=True, blank=True, on_delete = models.CASCADE)
    friday_lesson3 = models.ForeignKey(Lessons, related_name='friday_lesson3',null=True, blank=True, on_delete = models.CASCADE)
    friday_lesson4 = models.ForeignKey(Lessons, related_name='friday_lesson4',null=True, blank=True, on_delete = models.CASCADE)
    friday_lesson5 = models.ForeignKey(Lessons, related_name='friday_lesson5',null=True, blank=True, on_delete = models.CASCADE)
    friday_lesson6 = models.ForeignKey(Lessons, related_name='friday_lesson6',null=True, blank=True, on_delete = models.CASCADE)
    friday_lesson7 = models.ForeignKey(Lessons, related_name='friday_lesson7',null=True, blank=True, on_delete = models.CASCADE)
    friday_lesson8 = models.ForeignKey(Lessons, related_name='friday_lesson8',null=True, blank=True, on_delete = models.CASCADE)
    friday_lesson9 = models.ForeignKey(Lessons, related_name='friday_lesson9',null=True, blank=True, on_delete = models.CASCADE)
    #Суббота
    saturday_lesson1 = models.ForeignKey(Lessons, related_name='saturday_lesson1',null=True, blank=True, on_delete = models.CASCADE)
    saturday_lesson2 = models.ForeignKey(Lessons, related_name='saturday_lesson2',null=True, blank=True, on_delete = models.CASCADE)
    saturday_lesson3 = models.ForeignKey(Lessons, related_name='saturday_lesson3',null=True, blank=True, on_delete = models.CASCADE)
    saturday_lesson4 = models.ForeignKey(Lessons, related_name='saturday_lesson4',null=True, blank=True, on_delete = models.CASCADE)
    saturday_lesson5 = models.ForeignKey(Lessons, related_name='saturday_lesson5',null=True, blank=True, on_delete = models.CASCADE)
    saturday_lesson6 = models.ForeignKey(Lessons, related_name='saturday_lesson6',null=True, blank=True, on_delete = models.CASCADE)
    saturday_lesson7 = models.ForeignKey(Lessons, related_name='saturday_lesson7',null=True, blank=True, on_delete = models.CASCADE)
    saturday_lesson8 = models.ForeignKey(Lessons, related_name='saturday_lesson8',null=True, blank=True, on_delete = models.CASCADE)
    saturday_lesson9 = models.ForeignKey(Lessons, related_name='saturday_lesson9',null=True, blank=True, on_delete = models.CASCADE)
    #Воскресенье
    sunday_lesson1 = models.ForeignKey(Lessons, related_name='sunday_lesson1',null=True, blank=True, on_delete = models.CASCADE)
    sunday_lesson2 = models.ForeignKey(Lessons, related_name='sunday_lesson2',null=True, blank=True, on_delete = models.CASCADE)
    sunday_lesson3 = models.ForeignKey(Lessons, related_name='sunday_lesson3',null=True, blank=True, on_delete = models.CASCADE)
    sunday_lesson4 = models.ForeignKey(Lessons, related_name='sunday_lesson4',null=True, blank=True, on_delete = models.CASCADE)
    sunday_lesson5 = models.ForeignKey(Lessons, related_name='sunday_lesson5',null=True, blank=True, on_delete = models.CASCADE)
    sunday_lesson6 = models.ForeignKey(Lessons, related_name='sunday_lesson6',null=True, blank=True, on_delete = models.CASCADE)
    sunday_lesson7 = models.ForeignKey(Lessons, related_name='sunday_lesson7',null=True, blank=True, on_delete = models.CASCADE)
    sunday_lesson8 = models.ForeignKey(Lessons, related_name='sunday_lesson8',null=True, blank=True, on_delete = models.CASCADE)
    sunday_lesson9 = models.ForeignKey(Lessons, related_name='sunday_lesson9',null=True, blank=True, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.grade) + '"' + self.litera + '"'

class event(models.Model):
    starts_on = models.DateField()
    ends_on = models.DateField(blank=True,null=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    picture = models.ImageField()

class club_lesson(models.Model):
    name = models.CharField(max_length=20)
    club = models.CharField(max_length=20)
    teacher_id = models.IntegerField()
    classrom = models.CharField(max_length=20)
    day = models.CharField(max_length=20)
    lesson = models.IntegerField()
