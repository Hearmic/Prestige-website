from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from schedules.models import school_schedule,Lessons
from schollarsite.decorators import allowed_user_groups
from .forms import * 

# Create your views here.
def main(request):
    schedules = school_schedule.objects.all()  # Fetch all schedules
    context = {
        'schedules': schedules,
        'admin': ['Школьная администрация','Системный администратор']
    }
    return render(request, 'schedules/display.html', context)

def schedule_detail(request, grade, litera):
    schedule = get_object_or_404(school_schedule, grade=grade, litera=litera)
    context = {
        'schedule': schedule,
        'admin': ['Школьная администрация','Системный администратор']
        }
    return render(request, 'schedules/schedule_detail.html', context)

@allowed_user_groups(['Школьная администрация', 'Системный администратор'])
def create_schedule(request):
    form = SchoolScheduleForm(request.POST)
    errors = 'no error'
    context = {
        'form': form,
        'errors': errors
    }
    if request.method  == 'POST':
        if form.is_valid():
            grade = form.cleaned_data['grade']
            litera = form.cleaned_data['litera']
            # Проверить существующие расписания по классу и литере
            
            try:
                schedule = school_schedule.objects.get(grade=grade, litera=litera)
                # Обновление существующих полей
                # Понедельник
                schedule.monday_lesson1 = form.cleaned_data['monday_lesson1']
                schedule.monday_lesson2 = form.cleaned_data['monday_lesson2']
                schedule.monday_lesson3 = form.cleaned_data['monday_lesson3']
                schedule.monday_lesson4 = form.cleaned_data['monday_lesson4']
                schedule.monday_lesson5 = form.cleaned_data['monday_lesson5']
                schedule.monday_lesson6 = form.cleaned_data['monday_lesson6']
                schedule.monday_lesson7 = form.cleaned_data['monday_lesson7']
                schedule.monday_lesson8 = form.cleaned_data['monday_lesson8']
                schedule.monday_lesson9 = form.cleaned_data['monday_lesson9']
                # Вторник
                schedule.tuesday_lesson1 = form.cleaned_data['tuesday_lesson1']
                schedule.tuesday_lesson2 = form.cleaned_data['tuesday_lesson2']
                schedule.tuesday_lesson3 = form.cleaned_data['tuesday_lesson3']
                schedule.tuesday_lesson4 = form.cleaned_data['tuesday_lesson4']
                schedule.tuesday_lesson5 = form.cleaned_data['tuesday_lesson5']
                schedule.tuesday_lesson6 = form.cleaned_data['tuesday_lesson6']
                schedule.tuesday_lesson7 = form.cleaned_data['tuesday_lesson7']
                schedule.tuesday_lesson8 = form.cleaned_data['tuesday_lesson8']
                schedule.tuesday_lesson9 = form.cleaned_data['tuesday_lesson9']
                # Среда
                schedule.wednesday_lesson1 = form.cleaned_data['wednesday_lesson1']
                schedule.wednesday_lesson2 = form.cleaned_data['wednesday_lesson2']
                schedule.wednesday_lesson3 = form.cleaned_data['wednesday_lesson3']
                schedule.wednesday_lesson4 = form.cleaned_data['wednesday_lesson4']
                schedule.wednesday_lesson5 = form.cleaned_data['wednesday_lesson5']
                schedule.wednesday_lesson6 = form.cleaned_data['wednesday_lesson6']
                schedule.wednesday_lesson7 = form.cleaned_data['wednesday_lesson7']
                schedule.wednesday_lesson8 = form.cleaned_data['wednesday_lesson8']
                schedule.wednesday_lesson9 = form.cleaned_data['wednesday_lesson9']
                # Четверг
                schedule.thursday_lesson1 = form.cleaned_data['thursday_lesson1']
                schedule.thursday_lesson2 = form.cleaned_data['thursday_lesson2']
                schedule.thursday_lesson3 = form.cleaned_data['thursday_lesson3']
                schedule.thursday_lesson4 = form.cleaned_data['thursday_lesson4']
                schedule.thursday_lesson5 = form.cleaned_data['thursday_lesson5']
                schedule.thursday_lesson6 = form.cleaned_data['thursday_lesson6']
                schedule.thursday_lesson7 = form.cleaned_data['thursday_lesson7']
                schedule.thursday_lesson8 = form.cleaned_data['thursday_lesson8']
                schedule.thursday_lesson9 = form.cleaned_data['thursday_lesson9']
                # Пятница
                schedule.friday_lesson1 = form.cleaned_data['friday_lesson1']
                schedule.friday_lesson2 = form.cleaned_data['friday_lesson2']
                schedule.friday_lesson3 = form.cleaned_data['friday_lesson3']
                schedule.friday_lesson4 = form.cleaned_data['friday_lesson4']
                schedule.friday_lesson5 = form.cleaned_data['friday_lesson5']
                schedule.friday_lesson6 = form.cleaned_data['friday_lesson6']
                schedule.friday_lesson7 = form.cleaned_data['friday_lesson7']
                schedule.friday_lesson8 = form.cleaned_data['friday_lesson8']
                schedule.friday_lesson9 = form.cleaned_data['friday_lesson9']
                # Суббота
                schedule.sunday_lesson1 = form.cleaned_data['sunday_lesson1']
                schedule.sunday_lesson2 = form.cleaned_data['sunday_lesson2']
                schedule.sunday_lesson3 = form.cleaned_data['sunday_lesson3']
                schedule.sunday_lesson4 = form.cleaned_data['sunday_lesson4']
                schedule.sunday_lesson5 = form.cleaned_data['sunday_lesson5']
                schedule.sunday_lesson6 = form.cleaned_data['sunday_lesson6']
                schedule.sunday_lesson7 = form.cleaned_data['sunday_lesson7']
                schedule.sunday_lesson8 = form.cleaned_data['sunday_lesson8']
                schedule.sunday_lesson9 = form.cleaned_data['sunday_lesson9']
                # Воскресенье
                schedule.saturday_lesson1 = form.cleaned_data['saturday_lesson1']
                schedule.saturday_lesson2 = form.cleaned_data['saturday_lesson2']
                schedule.saturday_lesson3 = form.cleaned_data['saturday_lesson3']
                schedule.saturday_lesson4 = form.cleaned_data['saturday_lesson4']
                schedule.saturday_lesson5 = form.cleaned_data['saturday_lesson5']
                schedule.saturday_lesson6 = form.cleaned_data['saturday_lesson6']
                schedule.saturday_lesson7 = form.cleaned_data['saturday_lesson7']
                schedule.saturday_lesson8 = form.cleaned_data['saturday_lesson8']
                schedule.saturday_lesson9 = form.cleaned_data['saturday_lesson9']
                # Сохранение расписания
                schedule.save()
            except: # Создание нового расписания если такого еще не существует
                form.save()
        else:
            errors = form.errors
    return render (request, 'schedules/schedule_creation.html', context)

@allowed_user_groups(['Школьная администрация', 'Системный администратор'])
def create_lesson(request):
    form = LessonForm(request.POST)
    lessons = Lessons.objects.all()  # Получение всех уроков для выпадающего списка
    context = {
        'form': form,
        'admin': ['Школьная администрация','Системный администратор'],
        'lessons': lessons
    }
    if request.method  == 'POST':
        if form.is_valid:
            lesson = form.save(commit=False)
            lesson.lesson_type = form.cleaned_data['lesson_type']
            lesson.save()
            return redirect('schedules:create_lesson')
    return render (request, 'schedules/lesson_creation.html', context)

def lesson_details(request, lesson_id):
    lesson = Lessons.objects.get(pk=lesson_id)
    context = {
        'lesson': lesson
    }
    return render(request, 'schedules/lesson_details.html', context)