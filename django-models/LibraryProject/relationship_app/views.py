from django.shortcuts import render
from django.http import HttpResponse
from .models import Library, UserProfile
from .models import Book
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import permission_required, user_passes_test



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
    form_class = UserCreationForm()
    success_url = reverse_lazy(LoginView)
    template_name = "relationship_app/register.html"


@user_passes_test(UserProfile.role_choices("Admin"))
def admin_view(request):
    return HttpResponse("This user is an Admin")

@user_passes_test(UserProfile.role_choices("Librarian"))
def librarian_view(request):
    return HttpResponse("This user is a Librarian")

@user_passes_test(UserProfile.role_choices("Member"))
def member_view(request):
    return HttpResponse("This user is a member")
