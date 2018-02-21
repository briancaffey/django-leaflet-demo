from django.db.models import Q
from functools import reduce
from ..models import Book
import datetime

def filter_books(books, paramDict):
    # paramDict = request.GET
    params = paramDict.keys()

    # data filtering
    if any(x!='' for x in paramDict.values()):
        if paramDict['publish_date_after'] != '':
            after_date = paramDict['publish_date_after']
            _after_date = datetime.datetime.strptime(after_date, '%m/%d/%Y')
        
            books = books.filter(publish_date__gte=_after_date)

        if paramDict['publish_date_before'] != '':
            before_date = paramDict['publish_date_before']
            _before_date = datetime.datetime.strptime(before_date, '%m/%d/%Y')
            books = books.filter(publish_date__lte=_before_date)

        # filters records that contain any of the following keywords
        if paramDict['keywords'] != '':
            kws = paramDict['keywords'].split()
            q_lookups = [Q(title__icontains=kw) for kw in kws] + \
                        [Q(synopsis__icontains=kw) for kw in kws] + \
                        [Q(website__icontains=kw) for kw in kws]
            filters = Q()
            filters |= reduce(lambda x, y: x | y, q_lookups)
            books = books.filter(filters)

    return books