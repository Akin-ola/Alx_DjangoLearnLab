from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, CustomUser
from django.forms import ExampleForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import login, authenticate, hashers
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = get_object_or_404(CustomUser, email)
            print(user)
            if user:
                if hashers(password, user.password):
                    authenticated_user = authenticate(request, email=email, password=user.password)
                    print(authenticated_user)
                    if authenticated_user:
                        print(True)
                        login(request, user=user)
                        return redirect('book_list')
                else:
                    form.add_error(None, 'Email or Password is incorrect!')
            else:
                form.add_error('email', 'User with this email does not exist!')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
    

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, "bookshelf/list_books.html", context) 

@permission_required("bookshelf.can_create", raise_exception=True)
def edit_view(request):
    return render(request, "bookshelf/create.html")

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_view(request):
    return render(request, "bookshelf/edit.html")

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_view(request):
    return render(request, "bookshelf/delete.html")
