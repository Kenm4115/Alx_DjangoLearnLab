
from django.db import models

# Author model


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Library model


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

# Librarian model


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name
