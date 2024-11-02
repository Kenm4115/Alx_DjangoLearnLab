
from bookshelf.models import Book

#### Delete Operation (delete.md)

**Command**:
```python
retrieved_book.delete()
all_books = Book.objects.all()
print(all_books)  # Should be empty or not contain "Nineteen Eighty-Four"


# delete.md
```python
retrieved_book.delete()
all_books = Book.objects.all()
print(all_books)  # Outputs: <QuerySet []> indicating no books exist.

'''

Command: Delete the book you created and confirm the deletion by trying to retrieve all books again.
Document in: delete.md
Expected Documentation: Include the Python command and a comment with the expected output confirming the deletion.

'''