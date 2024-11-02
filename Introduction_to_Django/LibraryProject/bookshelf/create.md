
new_book = Book(title="1984", author="George Orwell", publication_year=1949)
new_book.save()


# create.md
```python
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
new_book.save()  # Book instance created successfully.


'''
Command: Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.
Document in: create.md
Expected Documentation: Include the Python command and a comment with the expected output noting the successful creation.

'''