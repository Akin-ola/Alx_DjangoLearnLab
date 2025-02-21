from django.urls import path
from .views import LibraryDetailView, list_book

urlpatterns = [
    # path("", view=list_book, name="home"),
    path("", view=LibraryDetailView.get_context_data)
]
