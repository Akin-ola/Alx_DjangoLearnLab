from django.urls import path
from .views import list_books, SignUpView, LoginView, LogoutView
from .views import LibraryDetailView

urlpatterns = [
    path("", view=list_books, name="home"),
    path("", view=LibraryDetailView.get_context_data),
    path("", view=SignUpView(template_name='relationship_app/register.html'), name='register'),
    path("", view=LoginView(template_name='relationship_app/login.html'), name='login'),
    path("", view=LogoutView(template_name='relationship_app/logout.html'), name='logout')  
]