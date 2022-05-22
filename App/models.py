from pickle import TRUE
from django.db import models        
from django.contrib.auth.models import User

class Genre(models.Model):
    title = models.CharField(max_length=50, unique=TRUE)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=500, null=True)
    genre = models.ManyToManyField(Genre, related_name='genre')
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=150, null=True)
    bookformat = models.CharField(max_length=150, null=True)
    isbn = models.CharField(max_length=150, null=True)
    pages = models.CharField(max_length=100, null=True)
    image =  models.URLField(null=True)
    # wishlist= models.ManyToManyField(User, related_name='wishlist')
    
    def __str__(self):
        return self.title

    @staticmethod
    def get_book_by_id(name):
        if name:
            return Book.objects.filter(genre = name)
        else:
            return Book.objects.all()
