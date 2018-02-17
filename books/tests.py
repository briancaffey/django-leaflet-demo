from django.test import TestCase
from .models import Book
from django.contrib.auth.models import User

# Create your tests here.

class SimpleTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

    def test_create_book(self):
        book = Book.objects.create(title="Test Book")
        all_books = Book.objects.all()
        self.assertEqual(len(all_books),1)
        first_book = all_books.first()
        self.assertIn("Test Book", first_book.title)