from django.shortcuts import render
from .serializers import PostSerializer, CommentSerializer, Comment, Post
from rest_framework import viewsets

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer