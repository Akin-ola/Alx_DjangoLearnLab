from .models import Author, Book, Library, Librarian

Author.objects.get(name=author_name)
Book.objects.filter(author=author)

Library.objects.get(name=library_name)
library_name.books.all()

Librarian.objects.filter(library=library)