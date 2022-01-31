from django.contrib import admin
from .models import Note

@admin.register(Note)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


