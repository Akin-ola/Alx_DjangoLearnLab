from .models import Author, Book, Library, Librarian

Book.objects.filter(author=author)

Library.objects.get(name=library_name)
library_name.books.all()

Librarian.objects.filter(library=library)