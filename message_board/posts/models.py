from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib import admin

class Post(models.Model):
    text = models.TextField()
    data = models.DateField(default=timezone.now)
    temperature = models.FloatField(default=0.0)
    pressure = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    wind_speed = models.IntegerField(default=0)
    
    def __str__(self):
        return self.text[:50]
    
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={"pk": self.pk})

class PostAdmin(admin.ModelAdmin):
    list_display = ["text", "data", "temperature", "pressure", "humidity", "wind_speed"]