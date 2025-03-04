from django.urls import path
from .views import LibraryDetailView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

     # URL pattern for the function-based view (list_books)
    path("book_list", views.list_books, name="book_list"),

     # URL pattern for the class-based view (LibraryDetailView)
    path("library_details", LibraryDetailView.as_view(), name="library_details"),

     # Authentication URLs
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),

     # Authenticated user views
    path("admin_view/", views.admin_view, name="admin_view"),
    path("librarian_view/", views.librarian_view, name="librarian_view"),
    path("member_view/", views.member_view, name="member_view"),

     # Secured URLs
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/<int:pk>/", views.edit_book, name="edit_book"),
    path("delete_book/<int:pk>/", views.delete_book, name="delete_book")
]