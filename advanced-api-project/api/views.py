from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics

# Create your views here.

class ListBookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [_isauthenticated]

class UpdateBookView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteBookView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
