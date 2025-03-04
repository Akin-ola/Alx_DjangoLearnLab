from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


""" Author model."""
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


""" Book model."""
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    class Meta:
        permissions=[
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book")
        ]


"""Library model."""
class Library(models.Model):
    name = models.CharField(max_length=50)
    book = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return f"{self.name}"

""" Librarian model."""
class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class UserProfile(models.Model):
    role_choices = [
    ("Admin", "Admin"),
    ("Librarian", "Librarian"),
    ("Member", "Member")
]
    role = models.CharField(choices=role_choices, default="Member",  max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Signal to create or update UserProfile whenever a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
