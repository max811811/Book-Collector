
from django.shortcuts import render

from .models import Book
# from .models import books as books

# class Book:
#     def __init__(self, name, genre, description, year):
#         self.name = name
#         self.breed = genre
#         self.description = description
#         self.age = year



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books })

def books_details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})