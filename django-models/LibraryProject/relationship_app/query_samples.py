from .models import Author, Book, Library, Librarian

Author.objects.get(name=author_name)

Library.objects.get(name=library_name)
library_name.books.all()

Librarian.objects.filter(library=library)