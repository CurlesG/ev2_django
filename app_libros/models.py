import re
from django.db import models
from sqlalchemy import null

# class Publisher(models.Model):
#     name = models.CharField(max_length=100, unique = True, null = False)
    
#     def __str__(self):
#         return self.name
    
# class Genre(models.Model):
#     name = models.CharField(max_length=100, unique = True, null = False)
#     # authors = models.ManyToManyField('Author', through='Book')
    
#     def __str__(self):
#         return self.name

# class Author(models.Model):
#     name = models.CharField(max_length=100, unique = True, null = False)
#     # genres = models.ManyToManyField('Genre', through = 'Book')
    
#     def __str__(self):
#         return self.name
    
# class Book(models.Model):
#     name = models.CharField(max_length=100, unique = True, null = False)
#     author = models.ManyToManyField('Author')
#     genre = models.ManyToManyField('Genre')
#     publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE)
    
#     def __str__(self):
#         return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100, unique = True, null = False)
    
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=100, unique = True, null = False)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100, unique = True, null = False)
    date_of_birth = models.DateField(default = null)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=100, unique = True, null = False)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, null = False)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE, null = False)
    publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name