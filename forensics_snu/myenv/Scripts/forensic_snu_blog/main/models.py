from django.db import models

# Create your models here.

class Write(models.Model):
    title = models.CharField(max_length=20) #제목최대길이 20자
    contents = models.TextField(max_length=500) #내용최대길이 500자
    created_at = models.DateTimeField(auto_now=True)