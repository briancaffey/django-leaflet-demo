from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, render_to_response
from django.utils.safestring import mark_safe
from django.utils.html import escapejs
from functools import reduce
from .forms import BookForm, QueryForm
from .models import Book
from .utils.filter import filter_books
from .utils.nearby import distance



import csv
import datetime
import json
import operator
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

    b_coords = (book.lon, book.lat)

    all_books = Book.objects.all()
    
    coords = [((b.lat, b.lon),b) for b in all_books]

    distance_dict = {}
    for c in coords:

        distance_dict[c[0]]=(distance(c[0],b_coords),c)

    

    sorted_nearby = sorted(distance_dict.items(), key=operator.itemgetter(1), reverse=False)[2]

    
    
    # f = itemgetter(2), the call f(r) returns r[2]

    map_book = [{'loc':[float(book.lon), float(book.lat)], 
                 'title':book.title, 
                 'url':book.get_absolute_url()}]
    context = {
        'book':book, 
        'map_book':mark_safe(escapejs(json.dumps(map_book))), 
        'sorted_nearby':sorted_nearby,
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




def viz(request):
    x= [1,3,5,7,9,11,13]
    y= [1,2,3,4,5,6,7]
    title = 'y = f(x)'

    plot = figure(title= title , 
        x_axis_label= 'X-Axis', 
        y_axis_label= 'Y-Axis', 
        plot_width =400,
        plot_height =400)

    plot.line(x, y, legend= 'f(x)', line_width = 2)
    #Store components 
    script, div = components(plot)

    #Feed them to the Django template.
    return render_to_response( 'books/viz.html',
            {'script' : script , 'div' : div} )