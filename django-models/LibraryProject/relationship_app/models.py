from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.models import Permission

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
    
    class Meta(Permission):
        Permissions=[
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book")
        ]





"""Library model."""
class Library(models.Model):
    name = models.CharField(max_length=50)
    book = models.ManyToManyField(Book, related_name="libraries")

""" Librarian model."""
class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)



class UserProfile(models.Model):
    role_choices = [
    ("Admin", "Admin"),
    ("Librarian", "Librarian"),
    ("Member", "Member")
]
    role = models.CharField(choices= role_choices, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
 