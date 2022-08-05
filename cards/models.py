from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.TextField(max_length=500)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
