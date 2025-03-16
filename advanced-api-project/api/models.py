from django.db import models

# Create your models here.
class Author(models.Model):   # An Author model that inherits from django models
    name = models.CharField(max_length=100)

class Book(models.Model):   # A Book model that inherits from django models
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, primary_key=False, on_delete=models.CASCADE)
    search_fields = ['title','author']