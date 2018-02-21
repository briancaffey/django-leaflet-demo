from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
from django.utils.html import escapejs
from functools import reduce
from .forms import BookForm, QueryForm
from .models import Book
from .utils.filter import filter_books

import csv
import datetime
import json
import xlwt
# Create your views here.

def all_books(request):
    """
    Main view for books. request.GET parameters are used to filter books
    """
    books = Book.objects.all()
    form = QueryForm(request.GET or None)
    paramDict = request.GET

    books = filter_books(books, paramDict)

    page_count = books.aggregate(Sum('pages'))

    map_books = [{'loc':[float(book.lon), float(book.lat)], 
                  'title':book.title,
                  'url':book.get_absolute_url()} for book in books]
    context = {
        'books':books,
        'map_books': mark_safe(escapejs(json.dumps(map_books))),
        'page_count':page_count['pages__sum'], 
        'form':form}
    return render(request, 'books/books.html', context)

def export_filtered_books_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Synopsis', 'Pages'])
    books = Book.objects.all()
    paramDict = request.GET
    print(paramDict)
    books = filter_books(books, paramDict)
    books = books.values_list(
        'title',
        'synopsis', 
        'pages')

    for book in books:
        writer.writerow(book)

    return response


def export_filtered_books_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="books.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Books')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Books', 'Synopsis', 'Pages']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    books = Book.objects.all()
    paramDict = request.GET
    books = filter_books(books, paramDict)
    rows = books.values_list('title', 'synopsis', 'pages')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def book_detail(request, id, slug):
    book = Book.objects.get(id=id, slug=slug)
    map_book = [{'loc':[float(book.lon), float(book.lat)], 
                 'title':book.title, 
                 'url':book.get_absolute_url()}]
    context = {
        'book':book, 
        'map_book':mark_safe(escapejs(json.dumps(map_book)))
    }
    return render(request, 'books/book_detail.html', context)

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
                publish_date=publish_date)
            book.save()
            return redirect('books:all')
    return render(request, 'books/new.html', {'form':form})