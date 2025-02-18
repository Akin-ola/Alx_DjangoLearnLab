from django.db import models

""" Author model."""
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

""" Book model."""
class Book(models.Model):
    book_title = models.CharField(max_length=50)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)

"""Library model."""
class Library(models.Model):
    library_name = models.CharField(max_length=50)
    book_title = models.ManyToManyField(Book, related_name="library")

""" Librarian model."""
class Librarian(models.Model):
    librarian_name = models.CharField(max_length=50)
    library_name = models.OneToOneField(Library, on_delete=models.CASCADE)



# Create your models here.
