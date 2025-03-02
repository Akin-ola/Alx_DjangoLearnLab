from django.urls import path
from .views import list_books
from .views import User_register, User_login, User_logout
from .views import LibraryDetailView

urlpatterns = [
    path("", view=list_books, name="home"),
    path("", LibraryDetailView.as_view(), name="library_details"),
    path("", User_register.as_view(), name="views.register"),
    path("", User_login.as_view(), name="login"),
    path("", User_logout.as_view(), name="logout"), 
]