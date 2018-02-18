from django.contrib import admin
from django.urls import path, re_path, include

from . import views

app_name = 'books'

urlpatterns = [
    
    re_path('^$', views.all_books, name="all"),
    re_path('^new/$', views.new_book, name="new"),
    re_path('^map_data/$', views.map_data, name="map_data"),
]
