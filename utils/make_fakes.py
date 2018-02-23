from authors.models import Author
from books.models import Book
from django.contrib.auth.models import User
import datetime
from faker import Faker 
import json
import random
from django.template.defaultfilters import slugify

User.objects.create_superuser(username='brian', password='qwer1234', email='briancaffey2010@gmail.com')


fake = Faker()

for i in range(100):
    name = fake.name().split()
    first_name = name[0]
    last_name = name[-1]
    author = Author.objects.create(
        first_name=first_name,
        last_name=last_name)
    author.save()


with open('utils/cities.json') as data_file:    
    data = json.load(data_file)


def make_synopsis(n):
    from faker import Faker 
    import random
    fake = Faker()
    synopsis = ""
    for i in range(n):
        synopsis += " ".join(fake.words(random.randint(10,20))).capitalize() + ". "
    return synopsis

all_authors = Author.objects.all()

for i in range(100):
    import random
    from faker import Faker 
    fake = Faker()
    title = " ".join([i.capitalize() for i in fake.words(3)])
    location = random.choice(data)
    lon = location['longitude']
    lon = float(str.format('{0:.6f}', float(lon)))
    lat = location['latitude']
    lat = float(str.format('{0:.6f}', float(lat)))
    pages = random.randint(100,3000)
    publish_date = fake.future_date()
    website = fake.url()
    slug = slugify(title)
    synopsis = make_synopsis(random.randint(4,7))
    status = True

    book = Book.objects.create(
        title=title,
        lon=lat,
        lat=lon,
        pages=pages,
        publish_date=publish_date,
        website=website,
        slug=slug,
        synopsis=synopsis,
        status=status
    )

    random_author = random.choice(all_authors)
    print(random_author)
    book.authors.add(random_author)
    book.save()
    # print(book.title)
    # print(book.authors.all())
    # print(book.lon, book.lat)
    





    # {'title':'My third book', 
    #  'lon':37,
    #  'lat':15,
    #  'pages':344, 
    #  'publish_date':datetime.datetime(2018, 7, 8, 12, 30),
    #  'website':'https://www.myfirstbook1.com', 
    #  'synopsis':'This is a third book also about Django', 
    #  'slug':'this-is-a-third-django-book',
    #  'status':True},

# ['_Generator__config', '_Generator__format_token', '_Generator__random', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add_provider', 'address', 'am_pm', 'ascii_company_email', 'ascii_email', 'ascii_free_email', 'ascii_safe_email', 'bank_country', 'bban', 'binary', 'boolean', 'bothify', 'bs', 'building_number', 'catch_phrase', 'century', 'chrome', 'city', 'city_prefix', 'city_suffix', 'color_name', 'company', 'company_email', 'company_suffix', 'country', 'country_code', 'credit_card_expire', 'credit_card_full', 'credit_card_number', 'credit_card_provider', 'credit_card_security_code', 'cryptocurrency_code', 'currency_code', 'date', 'date_between', 'date_between_dates', 'date_object', 'date_this_century', 'date_this_decade', 'date_this_month', 'date_this_year', 'date_time', 'date_time_ad', 'date_time_between', 'date_time_between_dates', 'date_time_this_century', 'date_time_this_decade', 'date_time_this_month', 'date_time_this_year', 'day_of_month', 'day_of_week', 'domain_name', 'domain_word', 'ean', 'ean13', 'ean8', 'email', 'file_extension', 'file_name', 'file_path', 'firefox', 'first_name', 'first_name_female', 'first_name_male', 'format', 'free_email', 'free_email_domain', 'future_date', 'future_datetime', 'geo_coordinate', 'get_formatter', 'get_providers', 'hex_color', 'iban', 'image_url', 'internet_explorer', 'ipv4', 'ipv6', 'isbn10', 'isbn13', 'iso8601', 'job', 'language_code', 'last_name', 'last_name_female', 'last_name_male', 'latitude', 'lexify', 'license_plate', 'linux_platform_token', 'linux_processor', 'locale', 'longitude', 'mac_address', 'mac_platform_token', 'mac_processor', 'md5', 'military_apo', 'military_dpo', 'military_ship', 'military_state', 'mime_type', 'month', 'month_name', 'msisdn', 'name', 'name_female', 'name_male', 'null_boolean', 'numerify', 'opera', 'paragraph', 'paragraphs', 'parse', 'password', 'past_date', 'past_datetime', 'phone_number', 'postalcode', 'postalcode_plus4', 'postcode', 'prefix', 'prefix_female', 'prefix_male', 'profile', 'provider', 'providers', 'pybool', 'pydecimal', 'pydict', 'pyfloat', 'pyint', 'pyiterable', 'pylist', 'pyset', 'pystr', 'pystruct', 'pytuple', 'random', 'random_digit', 'random_digit_not_null', 'random_digit_not_null_or_empty', 'random_digit_or_empty', 'random_element', 'random_int', 'random_letter', 'random_number', 'random_sample', 'random_sample_unique', 'randomize_nb_elements', 'rgb_color', 'rgb_css_color', 'safari', 'safe_color_name', 'safe_email', 'safe_hex_color', 'secondary_address', 'seed', 'seed_instance', 'sentence', 'sentences', 'set_formatter', 'sha1', 'sha256', 'simple_profile', 'slug', 'ssn', 'state', 'state_abbr', 'street_address', 'street_name', 'street_suffix', 'suffix', 'suffix_female', 'suffix_male', 'text', 'time', 'time_delta', 'time_object', 'time_series', 'timezone', 'tld', 'unix_time', 'uri', 'uri_extension', 'uri_page', 'uri_path', 'url', 'user_agent', 'user_name', 'uuid4', 'windows_platform_token', 'word', 'words', 'year', 'zipcode', 'zipcode_plus4']
