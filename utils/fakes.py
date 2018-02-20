import datetime
import faker
import random
import factory
from books.models import Book
from faker import Faker
fake = Faker()

class BookFactory(factory.Factory):
    
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words=4)
    lon = random.uniform(-180,180)
    lat = random.uniform(-90,90)
    pages = random.randint(20,2000)
    publish_date = fake.date_time_between(start_date="-10y", end_date="now", tzinfo=None)
    website = fake.url(schemes=None)

b = BookFactory.build()

print(b)