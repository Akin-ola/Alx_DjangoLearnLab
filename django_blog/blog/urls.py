from django.contrib.auth import views as v
from django.urls import path
from .views import (
    register, edit_profile, profile_view,
    PostCreateView, PostUpdateView, PostDeleteView, PostListView, PostDetailView
)
from . import views

urlpatterns = [
    path('login/', v.LoginView.as_view(template_name='blog/login.html'), name='login_view'),
    path('logout/', v.LogoutView.as_view(template_name='blog/logout.html'), name='logout_view'),
    path('register/', view=register, name='register_view'),
    path('profile/', view=profile_view, name='profile_view'),
    path('profile/edit/', view=edit_profile, name='profile_edit'),
    path('posts/', PostListView.as_view(), name='posts'),
    # path('posts/', views.post_list_view, name='posts'),
    # path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/new/', views.post_create_view, name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]