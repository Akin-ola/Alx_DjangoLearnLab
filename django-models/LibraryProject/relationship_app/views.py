from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, "relationship_app/list_books.html", context) 


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_details.html'

    def get_context_data(self):
        # context = super().get_context_data()
        context = self.get_object()
        context['librarian'] = library.get_librarian()