from django.contrib.auth import views
from django.urls import path
from .views import register, profile_view, edit_profile

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='blog/login.html'), name='login_view'),
    path('logout/', views.LogoutView.as_view(template_name='blog/logout.html'), name='logout_view'),
    path('register/', view=register, name='register_view'),
    path('profile/', view=profile_view, name='profile_view'),
    path('profile/edit/', view=edit_profile, name='profile_edit')
]
