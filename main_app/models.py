from django.db import models

# Create your models here.


class Book(models.Model):
  name = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  year = models.IntegerField()

  def __str__(self):
    return self.name




# books = [
#   Book('Halo', 'Space', 'A book about a space marines adventure', 2012),
#   Book('Raised by Wolves', 'Sci-Fi', 'a book about robots colonizing a planet with humans', 2018),
#   Book('Alchemist', 'adventure', 'a book about an italians trip to 15th century asia', 1578)
# ]