from django.urls import path
from .views import LibraryDetailView, list_books

urlpatterns = [
    path("", view=list_books, name="home"),
    path("", view=LibraryDetailView.get_context_data)
]
