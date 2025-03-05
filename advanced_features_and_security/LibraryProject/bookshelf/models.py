from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Group, User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book")
        ]


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(blank=True, null=True)
    groups= models.ManyToManyField(Group)
    user_permissions=None

    def __str__(self):
        return f"{self.username} : {self.email} {self.date_of_birth}"


class CustomUserManager(BaseUserManager):
    def create_user(self, username=None, password=None, email=None, is_staff=True, date_of_birth=None, profile_photo=None):
        pass
    
    def create_superuser(self, username=None, date_of_birth=None, profile_photo=None):
        pass

class UserProfile(models.Model):
    role_choices = [
    ("Admin", "Admin"),
    ("Librarian", "Librarian"),
    ("Member", "Member")
]
    role = models.CharField(choices=role_choices, default=None,  max_length=20)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class UserGroup(Group):
    """"""
    def __str__(self):
        return f"{self.name} : Permission(s) [{[].append(self.permissions)}]"


# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     instance.bookshelf_userprofile.save()

