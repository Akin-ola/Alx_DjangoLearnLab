from django.urls import path
from .views import list_books, RegisterView, LoginView, LogoutView
from .views import LibraryDetailView

urlpatterns = [
    path("", view=list_books, name="home"),
    path("", view=LibraryDetailView.get_context_data),
    path("", view=RegisterView(template_name='relationship_app/register.html'), name='views.register'),
    path("", view=LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path("", view=LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout')  
]