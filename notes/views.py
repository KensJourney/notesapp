from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

def all_notes(request):
    notes = Note.objects.all()
    return render(request, 'notes/home.html', {'notes': notes})