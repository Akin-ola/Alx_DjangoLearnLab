from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status, response.data 
from rest_framework import reverse
from .models import Book

# Create your tests here.


class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {'title': 'Sea', 'author': 'John Doe', 'publication_year': 2022}
        self.book = Book.objects.create(title='Habit', author='Jane Smith', publication_year=2020)

    @login_required
    def test_create_book(self):
        self.client.login
        response = self.client.post(reverse('book-list'), self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.id}), {'title': 'Updated Book'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
