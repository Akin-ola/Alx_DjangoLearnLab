from django.db import models
from django.contrib.auth.models import User 

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

"""Library model."""
class Library(models.Model):
    name = models.CharField(max_length=50)
    book = models.ManyToManyField(Book, related_name="libraries")

""" Librarian model."""
class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)


role_choices = [
    ("Admin"),
    ("Librarian"),
    ("Member")
]
class UserProfile(models.Model):
    role = models.CharField(choices= role_choices, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
 