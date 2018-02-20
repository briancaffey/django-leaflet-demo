from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.utils.html import escapejs
from django.db.models import Sum
from django.db.models import Q
from django.http import JsonResponse
from .forms import BookForm, QueryForm
import json
import datetime

from django.shortcuts import render, redirect
from .models import Book
# Create your views here.

def all_books(request):
    """
    Main view for books. request.GET parameters are used to filter books
    """
    books = Book.objects.all()
    form = QueryForm(request.GET or None)
    paramDict = request.GET
    params = paramDict.keys()
    
    # data filtering
    if request.GET != {}:
        if paramDict['publish_date_after']:
            after_date = paramDict['publish_date_after']
            _after_date = datetime.datetime.strptime(after_date, '%m/%d/%Y')
        
            books = books.filter(
                publish_date__gte=_after_date
            )

        if paramDict['publish_date_before']:
            before_date = paramDict['publish_date_before']
            _before_date = datetime.datetime.strptime(before_date, '%m/%d/%Y')

            books = books.filter(
                publish_date__lte=_before_date
            )

        if paramDict['keywords']:
            keywords = paramDict['keywords'].split()
            for kw in keywords:
                books = books.filter(
                    Q(title__contains=kw)
                )
                


    page_count = books.aggregate(Sum('pages'))
    map_books = [{'loc':[float(book.lon), float(book.lat)], 'title':book.title} for book in books]
    context = {
        'books':books,
        'map_books': mark_safe(escapejs(json.dumps(map_books))), # json.dumps(Decimal('3.9'), use_decimal=True)
        'page_count':page_count['pages__sum'], 
        'form':form}
    return render(request, 'books/books.html', context)

def map_data(request):
    books = Book.objects.all()
    book_list = [{"loc":[book.lon, book.lat], "title":book.title} for book in books]
    return JsonResponse({"data":book_list})

@login_required
def new_book(request):
    form = BookForm(None)
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            lon = form.cleaned_data['lon']
            lon = float(str.format('{0:.6f}', float(lon)))
            lat = form.cleaned_data['lat']
            lat = float(str.format('{0:.6f}', float(lat)))
            publish_date = form.cleaned_data['publish_date']
            pages = form.cleaned_data['pages']
            synopsis = form.cleaned_data['synopsis']
            book = Book(
                title=title, 
                lon=lon, 
                lat=lat, 
                synopsis=synopsis, 
                pages=pages, 
                publish_date=publish_date
                )
            book.save()
            return redirect('books:all')
    return render(request, 'books/new.html', {'form':form})