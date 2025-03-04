<!-- Create an instance of a book model and save it. -->
 book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
 book.save()