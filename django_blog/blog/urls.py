from django.contrib.auth import views
from django.urls import path
from .views import (
    register, edit_profile, profile_view,
    PostCreateView, PostDetailView, PostListView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='blog/login.html'), name='login_view'),
    path('logout/', views.LogoutView.as_view(template_name='blog/logout.html'), name='logout_view'),
    path('register/', view=register, name='register_view'),
    path('profile/', view=profile_view, name='profile_view'),
    path('profile/edit/', view=edit_profile, name='profile_edit')
]
urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_details'),
    path('posts/<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]