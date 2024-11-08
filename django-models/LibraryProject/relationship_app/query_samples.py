
import os
import django
from relationship_app.models import Author, Book, Library, Librarian

# Setup Django environment (useful for standalone script)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(f"Book Title: {book.title}, Author: {book.author.name}")

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f"Book Title: {book.title}, Library: {library.name}")

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian for {library.name}: {librarian.name}")

# Example usage:
# Query all books by a specific author
print("Books by Author 'J.K. Rowling':")
query_books_by_author("J.K. Rowling")

# List all books in a library
print("\nBooks in Library 'City Library':")
list_books_in_library("City Library")

# Retrieve the librarian for a library
print("\nLibrarian for 'City Library':")
retrieve_librarian_for_library("City Library")
