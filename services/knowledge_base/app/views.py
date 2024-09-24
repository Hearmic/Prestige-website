from django.shortcuts import redirect, render, get_object_or_404
from django_elasticsearch_dsl import search
from .decorators import allowed_user_groups
from .models import StudyMaterial, Subject, FavoriteMaterial, Answer, Question, MaterialType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .forms import AddStudyMaterialForm, QuestionForm, AnswerForm
# Далаир 11"В" и Ника Кавору были тут
@login_required
def home(request):

    query = request.GET.get('q')
    subject_filter = request.GET.get('subject')
    author_filter = request.GET.get('author')
    material_type_filter = request.GET.get('material_type')
    favorite_filter = request.GET.get('favorite')
    search_results = []

    if query:
        s = search.Search(index='study_material').query('multi_match', query=query, fields=['title', 'description', 'author.first_name','author.last_name', 'material_type.name'])
        if subject_filter:
            s = s.filter('term', subject__name=subject_filter)
        if author_filter:
            s = s.filter('term', author__id=author_filter)
        if material_type_filter:
            s = s.filter('term', material_type__id=material_type_filter)

        s = s.aggs.bucket('subjects', 'terms', field='subject.name')
        s = s.aggs.bucket('authors', 'terms', field='author.id')
        s = s.aggs.bucket('material_types', 'terms', field='material_type.id')

        response = s.execute()
        search_results = response.hits.hits

        # Преобразование результатов поиска в формат Django ORM для удобной пагинации
        search_results = [hit['_source'] for hit in search_results]
        materials = StudyMaterial.objects.filter(id__in=[result['id'] for result in search_results])

        aggregations = s.aggs.bucket('subjects', 'terms', field='subject.name')
        subject_buckets = aggregations.buckets['subjects']
        author_buckets = aggregations.buckets['authors']
        material_type_buckets = aggregations.buckets['material_types']

    else:
        materials = StudyMaterial.objects.order_by('-views')

    if favorite_filter:
        if query:
            materials = FavoriteMaterial.objects.filter(user=request.user, material__in=materials)
        else:
            materials = FavoriteMaterial.objects.filter(user=request.user)

    paginator = Paginator(materials, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except (EmptyPage, PageNotAnInteger):
        page_obj = paginator.page(1)

    context = {
        'subject_buckets': subject_buckets,
        'subject_filter': subject_filter,
        'author_buckets': author_buckets,
        'author_filter': author_filter,
        'material_type_buckets': material_type_buckets,
        'favorite_filter': favorite_filter,
        'page': page_obj,
        'materials': materials,
        'query': query,
        'total_results': response.hits.total.value if query else None
    }

    return render(request, 'knowledge_base/home.html', context)


@login_required
def material_detail(request, pk):

    material = get_object_or_404(StudyMaterial, pk=pk)
    files = material.files

    material.views += 1
    material.save()

    return render(request, 'knowledge_base/material_detail.html', {'material': material, 'files':files})

# Добавление материала в избранное (доступно только авторизованным пользователям)
@login_required
def add_to_favorites(request, pk):
    material = get_object_or_404(StudyMaterial, pk=pk)

    # Проверяем, есть ли уже этот материал в избранном у пользователя
    created = FavoriteMaterial.objects.get_or_create(user=request.user, material=material)

    if created:
        message = "Материал успешно добавлен в избранное."
    else:
        message = "Этот материал уже находится в вашем избранном." #TODO: Нужно придумать где отображать месседжы

    return render(request, 'knowledge_base/favorite_added.html', {'message': message})

@login_required
def favorite(request):
    favorite = FavoriteMaterial.objects.filter(user=request.user)
    return render(request, 'knowledge_base/favorite.html', {'favorite': favorite})

@login_required
def remove_from_favorites(request, pk):
    material = get_object_or_404(StudyMaterial, pk=pk)
    favorite = FavoriteMaterial.objects.filter(user=request.user, material=material)
    if favorite:
        favorite.delete()
        message = 'Материал был удален из избранного'
    else:
        message = 'Ошибка. Не удалось найти материал'
    return render(request, 'knowledge_base/favorite_removed.html', {'message': message})

@login_required
def subject_materials(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    material = get_object_or_404(StudyMaterial, subject=subject)
    return render(request, 'knowledge_base/subject_materials.html', {'subject': subject,'material': material})

@login_required
def favorite_materials(request):
    favorites = FavoriteMaterial.filter(user=request.user)
    context = {
        'favorites' : favorites , 
    }
    return render(request, 'knowledge_base/favorite_materials.html', context)

@login_required
@allowed_user_groups(allowed_groups=['Школьная администрация','Системный администратор','Учитель'])
def add_material(request):
    form = AddStudyMaterialForm(request.POST)
    if form.is_valid():
        material = form.save(commit=False)
        material.author = request.user
        material.save()
        return redirect('knowledge_base:home')
    return render(request, 'knowledge_base/add_study_material.html')

@login_required
@allowed_user_groups (allowed_groups=['Школьная администрация','Системный администратор', 'Учитель'])
def edit_material(request, pk):
    material = get_object_or_404(StudyMaterial, pk=pk)
    form = AddStudyMaterialForm(request.POST or None, instance=material)
    if form.is_valid():
        material = form.save(commit=False)
        material.save()
        return redirect('knowledge_base:material_detail', pk=material.pk)
    return render(request, 'knowledge_base/edit_study_material.html', {'form': form, 'material': material})

@login_required
@allowed_user_groups(allowed_groups=['Школьная администрация','Системный администратор', 'Учитель'])
def statistics_page(request):
        total_materials = StudyMaterial.objects.count()  
        total_subjects = Subject.objects.count()  
        most_viewed_material = StudyMaterial.objects.order_by('-views').first()  
        context= {
            'total_materials': total_materials,
            'total_subjects': total_subjects,
            'most_viewed_material': most_viewed_material
        }
        return render(request,'knowledge_base/statistics.html', context)
@login_required
def add_question(request, material_id):
    quiz = StudyMaterial.objects.get(id=material_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            return redirect('add_answers', question_id=question.id)
    else:
        form = QuestionForm()
    return render(request, 'quiz/add_question.html', {'form': form, 'quiz': quiz})

@login_required
def add_answers(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('add_answers', question_id=question_id)  # можно добавить несколько ответов
    else:
        form = AnswerForm()
    return render(request, 'quiz/add_answers.html', {'form': form, 'question': question})

@login_required
def take_quiz(request, material_id):
    quiz = StudyMaterial.objects.get(id=material_id)
    if request.method == 'POST':
        score = 0
        total_correct = 0
        for question in quiz.questions.all():
            selected_answer_id = request.POST.get(str(question.id))
            selected_answer = Answer.objects.get(id=selected_answer_id)
            if selected_answer.is_correct:
                score += 1
            total_correct += 1
        return render(request, 'quiz/quiz_result.html', {'score': score, 'total_correct': total_correct, 'quiz': quiz})
    return render(request, 'quiz/take_quiz.html', {'quiz': quiz})