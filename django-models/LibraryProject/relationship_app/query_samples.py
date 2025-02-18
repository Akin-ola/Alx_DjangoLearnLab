from .models import Author, Book, Library, Librarian

Author.books.all()

Library.objects.get(name="library_name")

Librarian.objects.filter(name="library_name")