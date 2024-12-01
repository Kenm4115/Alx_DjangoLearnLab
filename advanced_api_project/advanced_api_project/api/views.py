
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    """
    View to list all books with advanced filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # Fields to filter by
    search_fields = ['title', 'author__name']  # Fields to search on
    ordering_fields = ['title', 'publication_year']  # Fields for ordering
    ordering = ['title']  # Default ordering

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """View to retrieve a single book by ID."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    """View to create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Restrict to authenticated users only

    def perform_create(self, serializer):
        # Example: Custom logic before saving
        if serializer.validated_data['publication_year'] > 2024:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    """View to update an existing book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Restrict to authenticated users only

    def perform_update(self, serializer):
        # Example: Custom logic during update
        if serializer.validated_data.get('publication_year', 0) > 2024:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    """View to delete a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Restrict to authenticated users only


# Create your views here.
