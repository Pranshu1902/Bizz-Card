from django.db import models
from django.contrib.auth.models import User

# Create your models here.

color_choices = (("red", "red"), ("blue", "blue"), ("purple", "purple"))

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=100)
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    color = models.CharField(max_length=100)

class Links(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    link = models.URLField(max_length=500)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
