<!-- Retrieve and display a book you created -->
book = Book.objects.get(title="1984")
print(book)