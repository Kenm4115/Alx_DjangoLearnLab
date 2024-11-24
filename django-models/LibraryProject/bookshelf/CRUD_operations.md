
```markdown
# CRUD_operations.md

## Create
```python
new_book = Book(title="1984", author="George Orwell", publication_year=1949)
new_book.save()  # Book instance created successfully.

retrieved_book = Book.objects.get(title="1984")
print(retrieved_book)  # Outputs: 1984 by George Orwell, published in 1949

retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(retrieved_book.title)  # Outputs: Nineteen Eighty-Four

retrieved_book.delete()
all_books = Book.objects.all()
print(all_books)  # Outputs: <QuerySet []> indicating no books exist.
