from django.contrib.auth import views
from django.urls import path
from .views import register

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login_view'),
    path('logout/', views.LogoutView.as_view(template_name='logout.html'), name='logout_view'),
    path('register/', view=register, name='register_view')
]
