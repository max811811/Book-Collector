from django.db import models

# Create your models here.
class Book:
    def __init__(self, name, genre, description, year):
        self.name = name
        self.breed = genre
        self.description = description
        self.age = year

books = [
  Book('Halo', 'Space', 'A book about a space marines adventure', 2012),
  Book('Raised by Wolves', 'Sci-Fi', 'a book about robots colonizing a planet with humans', 2018),
  Book('Alchemist', 'adventure', 'a book about an italians trip to 15th century asia', 1578)
]
