from django.urls import path
from .views import all_notes

app_name = 'store'

urlpatterns = [
    path('', all_notes, name='all_notes'),
]