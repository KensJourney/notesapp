from django.db import models
from django.db import models
from django.urls import reverse
import datetime




class Note(models.Model):
    title = models.CharField(max_length=100, default="")
    body = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=255, default='admin')
    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Notes'
        ordering = ('-created_date',)


    def __str__(self):
        return self.title