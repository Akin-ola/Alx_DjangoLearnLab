from .models import Author, Book, Library, Librarian

Author.objects.get(name=author_name)

Library.objects.get(name=library_name)

Librarian.objects.filter(name="library_name")