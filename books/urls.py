from django.contrib import admin
from django.urls import path, re_path, include

from . import views

app_name = 'books'

urlpatterns = [
    
    re_path('^$', views.all_books, name="all"),
    re_path('^new/$', views.new_book, name="new"),
    re_path('^viz/$', views.viz, name="viz"),
    path('<int:id>/<slug:slug>/', views.book_detail, name="book_detail"),
    re_path('^csv/$', views.export_filtered_books_csv, name="csv"),
    re_path('^xls/$', views.export_filtered_books_xls, name="xls"),
]
