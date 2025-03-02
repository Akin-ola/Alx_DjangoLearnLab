from django.shortcuts import render
from .models import Library
from .models import Book
from django.views.generic import ListView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView



# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, "relationship_app/list_books.html", context) 


class LibraryDetailView(ListView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    

    # def library(self, request):
    #     library = self.get_queryset(Library.objects.all())
    #     context = {"library_details" : library} 
    #     return render(request, "relationship_app/library_detail.html", context)
        




class LoginView(LoginView):
    """"""

class LogoutView(LogoutView): 
    """"""

class User_register(CreateView):
    form_class = UserCreationForm("relationship_app/register.html")
    success_url = reverse_lazy(LoginView)
    template_name = "relationship_app/register.html"
