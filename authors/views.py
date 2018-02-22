from django.shortcuts import render
from .models import Author

# Create your views here.
def author_detail(request, id):
    author = Author.objects.get(id=id)
    context = {'author':author}
    return render(request, 'authors/author_detail.html', context)