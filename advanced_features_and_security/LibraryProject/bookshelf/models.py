from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
    

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} : {self.email} {self.date_of_birth}


class CustomUserManager(BaseUserManager):
    def create_user(self, username=None, password=None, email=None, date_of_birth=None, profile_photo=None):
        pass
    
    def create_superuser(self, username=None, date_of_birth=None, profile_photo=None):
        pass