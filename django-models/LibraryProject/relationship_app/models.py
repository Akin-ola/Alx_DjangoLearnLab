from django.db import models

""" Author model."""
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

""" Book model."""
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

"""Library model."""
class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name="libraries")

""" Librarian model."""
class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)



# Create your models here.
