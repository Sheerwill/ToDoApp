from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class ToDoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.CharField(max_length=100)