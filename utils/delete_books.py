from authors.models import Author
from books.models import Book
from django.contrib.auth.models import User

authors = Author.objects.all()

for author in authors:
    author.delete()

books = Book.objects.all()

for book in books:
    book.delete()

users = User.objects.all()

for user in users:
    user.delete()
