

#### Retrieve Operation (retrieve.md)

**Command**:
```python
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book)


# retrieve.md
```python
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book)  # Outputs: 1984 by George Orwell, published in 1949


'''
Command: Retrieve and display all attributes of the book you just created.
Document in: retrieve.md
Expected Documentation: Include the Python command and a comment with the expected output showing the details of the book.

'''