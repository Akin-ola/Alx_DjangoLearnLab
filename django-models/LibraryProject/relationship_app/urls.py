from django.urls import path
from .views import list_books, Admin_view, Librarian_view, Member_view
from .views import User_register, LoginView, LogoutView
from .views import LibraryDetailView

urlpatterns = [
    path("", view=list_books, name="home"),
    path("", LibraryDetailView.as_view(), name="library_details"),
    path("", User_register.as_view(), name="views.register"),
    path("", LoginView.as_view(template_name= "relationship_app/login.html"), name="login"),
    path("", LogoutView.as_view(template_name= "relationship_app/login.html"), name="logout"),
    path("", view=Admin_view, name="Admin"),
    path("", view=Librarian_view, name="Librarian"),
    path("", view=Member_view, name="Member")
]