from .models import Author, Book, Library, Librarian

Book.objects.filter(author=author)

Library.objects.get(name=library_name)

Librarian.objects.filter(library=library)