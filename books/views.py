from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .models import Book
# Create your views here.

def all_books(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'books/books.html', context)

@login_required
def new_book(request):
    if request.method == "POST":
        
        title = request.POST.get('title')
        book = Book(title=title)
        book.save()
        return redirect('books:all')

    return render(request, 'books/new.html', {})
