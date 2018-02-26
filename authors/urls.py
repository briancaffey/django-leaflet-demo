from django.contrib import admin
from django.urls import path, re_path, include

from . import views

app_name = 'authors'

urlpatterns = [
    
    # re_path('^$', views.all_books, name="all"),
    # re_path('^new/$', views.new_book, name="new"),
    re_path('^search_authors/$', views.search_authors, name="search_authors"),
    path('<int:id>/', views.author_detail, name="author_detail"),


]
