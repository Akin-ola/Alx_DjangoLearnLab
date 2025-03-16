from django.urls import path
from .views import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView
)

urlpatterns = [
    path('books/',  ListView.as_view(), name='book_list'),
    path('books/<int:pk>/', DetailView.as_view(), name='retrieve_book'),
    path('books/create/', CreateView.as_view(), name='create_book'),
    path('books/update/', UpdateView.as_view(), name='update_book'),
    path('books/delete/', DeleteView.as_view(), name='delete_book'),
]
