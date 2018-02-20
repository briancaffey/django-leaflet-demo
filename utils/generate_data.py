from books.models import Book
from django.contrib.auth.models import User
import datetime
import faker
import random
from faker import Faker
fake = Faker()


import factory
from books.models import Book

data = [
    {'title':'My first book', 
     'lon':41,
     'lat':13,
     'pages':230, 
     'publish_date':datetime.datetime(2005, 7, 14, 12, 30),
     'website':'https://www.myfirstbook.com', 
     'synopsis':'This is a book about Django', 
     'slug':'this-is-a-book-about-django',
     'status':True},

    {'title':'My second book', 
     'lon':33,
     'lat':12,
     'pages':540, 
     'publish_date':datetime.datetime(2008, 7, 8, 12, 30),
     'website':'https://www.myfirstbook.com', 
     'synopsis':'This is a second book also about Django', 
     'slug':'this-is-a-second-django-book',
     'status':True},

    {'title':'My third book', 
     'lon':37,
     'lat':15,
     'pages':344, 
     'publish_date':datetime.datetime(2018, 7, 8, 12, 30),
     'website':'https://www.myfirstbook1.com', 
     'synopsis':'This is a third book also about Django', 
     'slug':'this-is-a-third-django-book',
     'status':True},
]


User.objects.create_superuser(username='brian', password='qwer1234', email='briancaffey2010@gmail.com')

for b in data:
    book = Book.objects.create(
        title=b['title'],
        lon=b['lon'],
        lat=b['lat'],
        pages=b['pages'],
        publish_date=b['publish_date'],
        website=b['website'],
        synopsis=b['synopsis'],
        slug=b['slug'],
        status=b['status'],
    )
    book.save()

