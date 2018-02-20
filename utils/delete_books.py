from books.models import Book
from django.contrib.auth.models import User

users = User.objects.all()

for user in users:
    user.delete()

books = Book.objects.all()

for book in books:
    book.delete()