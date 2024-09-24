from datetime import timedelta
from django.db.models import Q
import qrcode
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render,redirect, get_object_or_404
from .models import exit_note
from .forms import ExitNoteForm
from django.contrib.auth.decorators import login_required
@login_required
def exit_notes_main(request):
    user = request.user
    form = ExitNoteForm()
    # Filter notes based on user relationships
    notes = exit_note.objects.filter(
        Q(created_by=user) |
        Q(created_by__in=user.parents.all()) |
        Q(created_by__head_teacher=user)
    )
    active_notes = notes.filter(parent_approved__isnull=False, teacher_approved__isnull=False, is_active=True)
    awaiting_confirmation_notes = notes.exclude(Q(parent_approved__isnull=False) & Q(teacher_approved__isnull=False) | Q(is_active=False) | Q(is_denied=True))
    denied_notes = notes.filter(is_denied=True, is_active=True)  
    context = {
                'active_notes': active_notes,
                'awaiting_confirmation_notes': awaiting_confirmation_notes,
                'denied_notes':denied_notes,
                'form': form,
            }
    if request.method == 'POST':
        form = ExitNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = request.user
            note.deactivate_on = timezone.now() + timedelta(hours=1)
            note.save()

            return render (request,'exit_notes/exit_notes_main.html', context)
        else:
            pass
    else:
        return render(request,'exit_notes/exit_notes_main.html', context )

@login_required
def deactivate_expired_notes():
    now = timezone.now()
    expired_notes = exit_note.objects.filter(deactivate_on__lte=now, is_active=True)
    for note in expired_notes:
        note.is_active = False
        note.save()
        
@login_required
def exit_notes_details(request, note_id):
    note = exit_note.objects.get(pk=note_id)
    context = {
        'note': note,
        'moderators': ['Модератор предложений','Школьная администрация','Системный администратор'],
        'students': ['Ученик'],
        'teachers': ['Учитель','Классный руководитель', 'Завуч'],
        'parents':['Родитель']
        }
    return render (request, 'exit_notes/exit_note_details.html' , context)

@login_required
def parent_approve(request,note_id):
    note = exit_note.objects.get(pk=note_id)
    user = request.user
    note.parent_approved = user
    note.save()

@login_required
def teacher_approve(request,note_id):
    note = exit_note.objects.get(pk=note_id)
    user = request.user
    note.teacher_approved = user
    note.save()
    context = {
        'note': note,
        'moderators': ['Модератор предложений','Школьная администрация','Системный администратор'],
        'students': ['Ученик'],
        'teachers': ['Учитель','Классный руководитель', 'Завуч'],
        'parents':['Родитель']
        }
    return render(request, 'exit_notes/exit_note_details.html', context)

@login_required
def security_approve(request,note_id):
    note = exit_note.objects.get(pk=note_id)
    user = request.user
    note.security_approved = user
    note.is_active = False
    note.save()
    context = {
        'note': note,
        'moderators': ['Модератор предложений','Школьная администрация','Системный администратор'],
        'students': ['Ученик'],
        'teachers': ['Учитель','Классный руководитель', 'Завуч'],
        'parents':['Родитель'],
        'security':['Безопасность','Охранник']
        }
    return render(request, 'exit_notes/exit_note_details.html', context)

@login_required 
def generate_qr_code(request, note_id):
    note = get_object_or_404(exit_note, id=note_id)
    url = request.build_absolute_url(note.get_absolute_url())
    qr = qrcode.make(url)
    response = HttpResponse(content_type='image/png')
    note.qr_code = response
    return response

@login_required
def deny(request, note_id):
    note = exit_note.objects.get(pk=note_id)
    user = request.user
    note.is_denied = True
    note.denied_by = user
    note.save()
    context = {
        'note': note,
        'moderators': ['Модератор предложений','Школьная администрация','Системный администратор'],
        'students': ['Ученик'],
        'teachers': ['Учитель','Классный руководитель', 'Завуч'],
        'parents':['Родитель']
        }
    return render(request, 'exit_notes/exit_note_details.html', context)

@login_required
def exit_notes_delete(request, note_id):
    note = exit_note.objects.get(pk=note_id)
    note.is_active = False
    note.save()
    return redirect('exit_notes:exit_notes')

@login_required
def how_it_works(request):
    context = {
        'moderators': ['Модератор предложений','Школьная администрация','Системный администратор'],
        'students': ['Ученик'],
        'teachers': ['Учитель','Классный руководитель', 'Завуч'],
        'parents':['Родитель']
        }
    return render (request, 'exit_notes/how_it_works.html' , context)