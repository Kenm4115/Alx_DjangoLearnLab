
from relationship_app.models import Library, Librarian
import os
import django
from relationship_app.models import Author, Book, Library

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


# Replace 'library_name_here' with the actual name of the library you're querying.
library_name = 'library_name_here'

try:
    # Get the specific library by its name
    library = Library.objects.get(name=library_name)

    # Retrieve the librarian associated with this library
    librarian = Librarian.objects.get(library=library)

    # Print the librarian's details
    print(f"Librarian for {library.name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"No library found with the name '{library_name}'.")
except Librarian.DoesNotExist:
    print(f"No librarian is assigned to the library '{library_name}'.")


# def retrieve_librarian_for_library(library_name):
#     library = Library.objects.get(name=library_name)
#     librarian = library.librarian
#     print(f"Librarian for {library.name}: {librarian.name}")


# Example usage:
# Query all books by a specific author
print("Books by Author 'J.K. Rowling':")
query_books_by_author("J.K. Rowling")

# List all books in a library
print("\nBooks in Library 'City Library':")
list_books_in_library("City Library")

# # Retrieve the librarian for a library
# print("\nLibrarian for 'City Library':")
# retrieve_librarian_for_library("City Library")
