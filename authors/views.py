from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Author

import json

# Create your views here.
def author_detail(request, id):
    author = Author.objects.get(id=id)
    context = {'author':author}
    return render(request, 'authors/author_detail.html', context)

def search_authors(request):
    if request.is_ajax():
        print(request.GET)
        q = request.GET.get('term', '')
        authors = Author.objects.filter(full_name__icontains = q)[:10]
        results = []
        for author in authors:
            author_json = {}
            author_json['id'] = author.full_name 
            author_json['label'] = author.full_name 
            author_json['value'] = author.full_name 
            results.append(author_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)