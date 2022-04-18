


from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import ReadingForm

from .models import Book, Store
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
    print(book)
    id_list = book.stores.all().values_list('id')
    print(id_list)
    store_book_not_at = Store.objects.exclude(id__in=id_list)
    print(store_book_not_at)
    reading_form = ReadingForm()
    return render(request, 'books/detail.html', {'book': book, 'reading_form': reading_form, 'stores': store_book_not_at})

def add_reading(request, book_id):
  # create a ModelForm instance using the data in request.POST
  form = ReadingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_reading = form.save(commit=False)
    new_reading.book_id = book_id
    new_reading.save()
  return redirect('details', book_id=book_id)

def assoc_store(request, book_id, store_id):
    Book.objects.get(id=book_id).stores.add(store_id)
    return redirect('details', book_id=book_id)

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'type', 'description', 'year']
    success_url = '/books/'

class BookUpdate(UpdateView):
    model = Book 
    fields = ['genre', 'description', 'year']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

# stores below--------------------------------------

class StoreList(ListView):
  model = Store

class StoreDetail(DetailView):
  model = Store

class StoreCreate(CreateView):
  model = Store
  fields = '__all__'

class StoreUpdate(UpdateView):
  model = Store
  fields = ['name', 'location']

class StoreDelete(DeleteView):
  model = Store
  success_url = '/stores/'