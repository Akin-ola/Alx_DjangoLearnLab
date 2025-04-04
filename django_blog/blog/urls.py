from django.contrib.auth import views as v
from django.urls import path
from . import views

urlpatterns = [
    path('login/', v.LoginView.as_view(template_name='blog/login.html'), name='login'),
    # path('logout/', v.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    # path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    # path('posts/', views.PostListView.as_view(), name='posts'),
    # path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    # path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    # path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    # path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    # path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='profile_edit'),
    path('post/new/', views.post_create_view, name='post_create'),
    path('posts/', views.post_list_view, name='posts'),
    path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('post/<int:pk>/update/', views.update_post_view, name='post_update'),
    path('post/<int:pk>/delete/', views.delete_post_view, name='post_delete'),
    path('comment/<int:pk>/update/', views.update_comment_view, name='comment_update'),
    path('comment/<int:pk>/delete/', views.delete_comment_view, name='comment_delete'),
]