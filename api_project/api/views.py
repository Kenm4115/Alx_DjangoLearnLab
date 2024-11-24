from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics.ListAPIView
from rest_framework.viewsets.ModelViewSet


class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieve all Book objects
    serializer_class = BookSerializer  # Use the BookSerializer for serialization

class BookViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations for the Book model.
    """
    queryset = Book.objects.all()  # Retrieve all Book objects
    serializer_class = BookSerializer  # Use the BookSerializer for data validation and representation
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users
