from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500)
    profile_picture = models.ImageField()
    followers = models.ManyToManyField('CustomUser', symmetrical=False)
