from django.urls import path
from .views import (
    ListBookView,
    CreateBookView,
    DeleteBookView,
    DetailView,
    UpdateBookView
)

urlpatterns = [
    path('books/',  ListBookView.as_view(), name='book_list'),
    path('books/<int:pk>/', DetailView.as_view(), name='retrieve_book'),
    path('books/create/', CreateBookView.as_view(), name='create_book'),
    path('books/update/', UpdateBookView.as_view(), name='update_book'),
    path('books/delete/', DeleteBookView.as_view(), name='delete_book'),
]
