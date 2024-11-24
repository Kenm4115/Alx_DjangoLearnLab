
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)  # Title of the book
    author = models.CharField(max_length=255)  # Author of the book

    def __str__(self):
        return f"{self.title} by {self.author}"
