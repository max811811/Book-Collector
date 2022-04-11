
from django.shortcuts import render

from django.http import HttpResponse
from .models import books as books


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello book </h1>')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    return render(request, 'books/index.html', {'books': books })