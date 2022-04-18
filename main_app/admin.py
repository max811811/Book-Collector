from django.contrib import admin
# # import your models here
from .models import Book, Reading

# # Register your models here
admin.site.register(Book)
admin.site.register(Reading)