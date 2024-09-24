from datetime import timedelta
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, redirect, render
from datetime import date

        
# Create your views here.
def display_menu (request):
    today = date.today()
    try:
        # Get the WeeklyMenus object where starts_on is before today and ends_on is after today
        menu = WeeklyMenus.objects.get(starts_on__lte=today, ends_on__gte=today)
    except WeeklyMenus.DoesNotExist:
        menu = None
    context = {'menu': menu,
                'canteen_worker': ['Работник столовой']}
    return render(request, 'menu/menu_main.html', context)  


def display_menu_list(request):
    menus = WeeklyMenus.objects.all()
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'menus': menus,
                'form': form
            }
            return render(request, 'menu/menu_list.html', context)
    else:
        form = MenuForm()

    context = {
        'menus': menus,
        'form': form
    }
    return render(request, 'menu/menu_list.html', context)

    
def update_menu (request, menu_id) :
    
    if request.method == 'POST':
        form = MenuForm(request.POST)
        menu = get_object_or_404(WeeklyMenus, pk=menu_id)
        if form.is_valid():
            starts_on= form.cleaned_data['starts_on']
            #Обновление миню. Если в форме выбранно *none* то значение оcтанеться прежним
            menu.update(
                #----------------------------Завтраки---------------------------------------------
                monday_breakfast=form.cleaned_data ['monday_breakfast'],
                tuesday_breakfast=form.cleaned_data ['tuesday_breakfast'],
                wednesday_breakfast=form.cleaned_data ['wednesday_breakfast'],
                thursday_breakfast=form.cleaned_data ['thursday_breakfast'],
                friday_breakfast=form.cleaned_data ['friday_breakfast'],
                saturday_breakfast=form.cleaned_data ['saturday_breakfast'],
                sunday_breakfast=form.cleaned_data ['sunday_breakfast'],
                #----------------------------Обеды------------------------------------------------
                monday_lunch=form.cleaned_data ['monday_lunch'],
                tuesday_lunch=form.cleaned_data ['tuesday_lunch'],
                wednesday_lunch=form.cleaned_data ['wednesday_lunch'],
                thursday_lunch=form.cleaned_data ['thursday_lunch'],
                friday_lunch=form.cleaned_data ['friday_lunch'],
                saturday_lunch=form.cleaned_data ['saturday_lunch'],
                sunday_lunch=form.cleaned_data ['sunday_lunch'],
                #----------------------------Ужины------------------------------------------------
                monday_dinner=form.cleaned_data ['monday_dinner'],
                tuesday_dinner=form.cleaned_data ['tuesday_dinner'],
                wednesday_dinner=form.cleaned_data ['wednesday_dinner'],
                thursday_dinner=form.cleaned_data ['thursday_dinner'],
                friday_dinner=form.cleaned_data ['friday_dinner'],
                saturday_dinner=form.cleaned_data ['saturday_dinner'],
                sunday_dinner=form.cleaned_data ['sunday_dinner'],
                #---------------------------Обновление дат-----------------------------------------
                starts_on = starts_on,
                ends_on = starts_on + timedelta(days = 7)
            )
        else :
            return render(request, 'canteen_menu:create_menu.html', {'form': form, 'menu': menu})

#---------------------------------------------------Добавление аллергий----------------------------------------------------------

def create_allergies(request):
    form =AddAllergieForm(request.POST)
    object = allergies.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            allergie = form.save(commit=False)
            allergie.save()
            return redirect ('menu:allergies_list')  # Redirect to list view after successful creation
    else:
        return render(request, 'menu/create_allergies.html',{'form': form, 'allergies': object})

def delete_allergies(request, allergies_id):
    allergie = allergies.objects.filter(pk = allergies_id)
    allergie.delete()
    return redirect('menu:allergies_list')  

#---------------------------------------------------Чпичок всех блюд и напитков--------------------------------------------------
def dish_list (request):
    breakfast_dishes = dish.objects.filter(type = "Завтрак")
    lunch_dishes = dish.objects.filter(type = "Обед")
    dinner_dishes = dish.objects.filter(type = "Полдник")
    breakfast_drinks = drink.objects.filter(type = "Завтрак")
    lunch_dirinks = drink.objects.filter(type = "Обед")
    dinner_drinks = drink.objects.filter(type = "Полдник")
    breakfast_mealsets = breakfast_MealSet.objects.all
    lunch_mealsets =  lunch_MealSet.objects.all
    dinner_mealsets = dinner_MealSet.objects.all
    context= {
        'lunch_dishes': lunch_dishes,
        'dinner_dishes': dinner_dishes,
        'breakfast_dishes': breakfast_dishes,
        'breakfast_drinks':breakfast_drinks,
        'lunch_drinks':lunch_dirinks,
        'dinner_drinks':dinner_drinks,
        'breakfast_mealsets':breakfast_mealsets,
        'lunch_mealsets':lunch_mealsets,
        'dinner_mealsets':dinner_mealsets,
        'canteen_worker' : 'Работник столовой',
        'system_administration': 'Системный администратор',
    }
    return render(request, 'menu/dishes_list.html', context)

#------------------------------------------------- Добавление блюд ------------------------------------------------------------

def create_dish(request):
    return render(request, 'menu/creation_choice_dishes.html')

#------------------------------------------------- Добавление напитков ------------------------------------------------------------

def create_drink(request):
    form = DrinkForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            drink = form.save(commit=False)
            drink.save()
            return redirect('menu:dishes_list')
    else:
        return render(request,'menu/create_form.html',{'form':form})


#------------------------------------------------------Список наборов блюд-----------------------------------------------------
def MealSet_list (request):
    breakfast_sets = breakfast_MealSet.objects.all()
    lunch_sets = lunch_MealSet.objects.all()
    dinner_sets = dinner_MealSet.objects.all()
    context= {
        
        'lunch_sets': lunch_sets,
        'dinner_sets': dinner_sets,
        'breakfast_sets': breakfast_sets,
        'canteen_workers' : ['Работник столовой'],
        'canteen_moderator' : ['Системный администратор']
    }
    return render(request,'menu/sets_list.html', context)
#------------------------------------------------------Создание наборов блюд-----------------------------------------------------

def create_set (request):
    return render(request, 'menu/creation_choice_sets.html')
#---На завтрак---#
def create_breakfast_set (request):
    form = BreakfastSetForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            set = form.save(commit=False)
            set.save()
            return redirect('menu:sets_list')
    else:
        return render (request,'menu/create_form.html', {'form': form})
    
#---На обед---#
def create_lunch_set (request):
    form = LunchSetForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            set = form.save(commit=False)
            set.save()
            return redirect('menu:sets_list')
    else:
        return render (request,'menu/create_form.html', {'form': form})

#---На полдник---#
def create_dinner_set (request):
    form = DinnerSetForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            set = form.save(commit=False)
            set.save()
            return redirect('menu:sets_list')
    else:
        return render (request,'menu/create_form.html', {'form': form})
#------------------------------------------------------Обновление наборов--------------------------------------------------------

#---На завтрак---#
def update_breakfast_MealSet(request,MealSet_id):
    if request.method == 'POST':
        form = BreakfastSetForm(request.POST)
        MealSet = get_object_or_404(breakfast_MealSet, pk= MealSet_id)
        if form.is_valid():
            MealSet.update(
                dishes = form.cleaned_data['dishes'],
                drink = form.cleaned_data['drink'],
                name = form.cleaned_data['name']
            )
            
            return redirect('menu:sets_list')
    else:
        return render (request,'menu/create_form.html', {'form': form})
    
#---На обед---#    
def update_lunch_MealSet(request, MealSet_id):
    if request.method == 'POST':
        form = LunchSetForm(request.POST)
        MealSet = get_object_or_404(lunch_MealSet, pk= MealSet_id)
        if form.is_valid():
            MealSet.update(
                dishes = form.cleaned_data['dishes'],
                drink = form.cleaned_data['drink'],
                name = form.cleaned_data['name']
            )
            
            return redirect('menu:sets_list')
    else:
        return render (request,'menu/create_form.html', {'form': form})
    
#---На полдник---#
def update_dinner_MealSet(request, MealSet_id):
    if request.method == 'POST':
        form = DinnerSetForm(request.POST)
        MealSet = get_object_or_404(dinner_MealSet, pk= MealSet_id)
        if form.is_valid():
            MealSet.update(
                dishes = form.cleaned_data['dishes'],
                drink = form.cleaned_data['drink'],
                name = form.cleaned_data['name']
            )
            
            return redirect('menu:sets_list')
    else:
        return render (request,'menu/create_form.html', {'form': form})
