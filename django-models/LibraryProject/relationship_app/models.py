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

    def __str__(self):
        return self.title

"""Library model."""
class Library(models.Model):
    name = models.CharField(max_length=50)
    book = models.ManyToManyField(Book, related_name="libraries")

""" Librarian model."""
class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)


# Testing the models relationships.

# author1 = Author.objects.create(name="Akin")
# author2 = Author.objects.create(name="Tunji")

# book1 = Book.objects.create(title="sea", author = author1)
# book2 = Book.objects.create(title="rise", author = author2)
# book3 = Book.objects.create(title="Crow", author = author2)

# Book.objects.filter(author=author2)

# library1=Library.objects.create(name="Yisa Doko")
# library2=Library.objects.create(name="Ibrahim Alfa")

# library1.book.add(book1)
# library1.book.add(book2)

# library1.books.all()

# librarian1 = Librarian.objects.create(name="max",library=library1)
# librarian2 = Librarian.objects.create(name="john", library=library2)

# Create your models here.
