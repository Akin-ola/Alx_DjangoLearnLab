from .models import Author, Book, Library, Librarian

Book.objects.filter(author=author)

library_name.books.all()

Librarian.objects.filter(library=library)