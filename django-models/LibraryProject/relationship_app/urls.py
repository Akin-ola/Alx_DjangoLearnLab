from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", view=list_books, name="home"),
    path("", view=LibraryDetailView.get_context_data)
]

urlpatterns = [
    path("", LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path("", LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout')  
]