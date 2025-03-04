from bookshelf.models import Book

<!-- Delete the book instance you created in the book model. -->
Book.object.delete(title="1984")