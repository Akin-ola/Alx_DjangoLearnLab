from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookDeleteView,
    BookRetrieveView,
    BookUpdateView
)

urlpatterns = [
    path('books/',  BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookRetrieveView.as_view(), name='retrieve_book'),
    path('books/delete/', BookDeleteView.as_view(), name='delete_book'),
    path('books/update/', BookUpdateView.as_view(), name='update_book'),
    path('books/create/', BookCreateView.as_view(), name='create_book'),
]
