from django.shortcuts import render
from .models import Library
from django.views.generic.detail import DetailView
from .models import Book

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, "relationship_app/list_books.html", context) 


class LibraryDetailView(DetailView):
    
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self):
        # context = super().get_context_data()
        context = self.get_object()
        context['librarian'] = library.get_librarian()

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('Login')
    template_name = 'relationship_app/register.html'

class LoginView(CreateView):
    model = login
    template_name = "relationship_app/login.html"

class LogoutView(CreateView):
    model = logout
    template_name = "relationship_app/logout.html"