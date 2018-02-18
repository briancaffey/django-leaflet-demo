from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.shortcuts import render, redirect
from .models import Book
# Create your views here.

def all_books(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'books/books.html', context)

def map_data(request):
    books = Book.objects.all()
    book_list = [{"loc":[book.lon, book.lat], "title":book.title} for book in books]
    return JsonResponse({"data":book_list})


@login_required
def new_book(request):
    if request.method == "POST":
        
        title = request.POST.get('title')
        lon = request.POST.get('lon')
        lat = request.POST.get('lat')
        book = Book(title=title, lon=lon, lat=lat)
        book.save()
        return redirect('books:all')

    return render(request, 'books/new.html', {})
