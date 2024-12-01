
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),               # ListView
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # DetailView
    path('books/create/', BookCreateView.as_view(), name='book-create'),    # CreateView
    path('books/update/', BookUpdateView.as_view(), name='book-update'),  # UpdateView
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),  # DeleteView
]
