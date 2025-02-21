from django.urls import path
from .views import list_books


urlpatterns = [
    path("", view=list_books, name="home"),
    path("", view=LibraryDetailView.get_context_data)
]
