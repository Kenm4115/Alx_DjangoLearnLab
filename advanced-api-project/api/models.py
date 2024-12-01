

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE,) # Author of the book

    def __str__(self):
        return self.title




# Create your models here.


# Create your models here.
