from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post_all', PostViewSet, basename='post_all')
router.register(r'comment_all', CommentViewSet, basename='comment_all')

urlpatterns = [
    path('', include(router.urls)),
]
