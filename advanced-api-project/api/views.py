from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters import rest_framework

# Create your views here.

class ListView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, rest_framework.DjangoFilterBackend,]
    filterset_fields = ['title', 'book__author']
    ordering_fields = ['title', 'book__author']

    def get_queryset(self):
        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        publication_year = self.request.query_params.get('publication_year')
        if title is not None:
            queryset = queryset.filter(book_title=title)
        elif author is not None:
            queryset = queryset.filter(book__author=author)
        elif publication_year is not None:
            queryset = queryset.filter(book_publication_year=publication_year)
        return queryset

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'book__author',]

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
