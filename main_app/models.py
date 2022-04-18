from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

RATINGS = (
  ('A', 'Great'),
  ('B', 'Medium'),
  ('C', 'Poor'),
)







class Store(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  location = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('stores_detail', kwargs={'pk': self.id})

class Book(models.Model):
  name = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  year = models.IntegerField()

  stores = models.ManyToManyField(Store)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'book_id': self.id})

class Reading(models.Model):
  print(models)
  date = models.DateField('Reading date')
  rating = models.CharField(
    max_length=1,
    choices=RATINGS,
    default=RATINGS[0][0],
    )

  book = models.ForeignKey(Book, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_rating_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

