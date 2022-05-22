from django.contrib import admin
from .models import Book,Genre
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Genre)
admin.site.register(Book)