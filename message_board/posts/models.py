from django.utils import timezone
from django.db import models
from django.contrib import admin

class Post(models.Model):
    text = models.TextField()
    data = models.DateField(default=timezone.now)
    temperature = models.FloatField(default=0.0)
    preseure = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.text[:50]

class PostAdmin(admin.ModelAdmin):
    list_display = ["text", "data", "temperature", "preseure", "humidity"]