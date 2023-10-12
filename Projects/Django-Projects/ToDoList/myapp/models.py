from django.db import models
# Create your models here.

class Tasks(models.Model):
    task = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
