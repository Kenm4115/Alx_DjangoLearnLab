
# API Endpoints

## Book Endpoints
- **List all books:** `GET /api/books/`
- **Retrieve a book by ID:** `GET /api/books/<id>/`
- **Create a book (authenticated):** `POST /api/books/create/`
- **Update a book (authenticated):** `PUT /api/books/<id>/update/`
- **Delete a book (authenticated):** `DELETE /api/books/<id>/delete/`

## Permissions
- Read-only access for unauthenticated users.
- Create, update, and delete require authentication.

## Customizations
- Validates that `publication_year` is not in the future during creation and update.
- Filters available for `author` and `publication_year` on the list view.

# Advanced Querying in the Book API

## Filtering
Use query parameters to filter books:
- `title`: Filter by title.
- `author`: Filter by author's ID.
- `publication_year`: Filter by publication year.
Example: `/api/books/?title=Harry Potter&publication_year=1997`

## Searching
Perform a text search:
- `search`: Search books by title or author's name.
Example: `/api/books/?search=Rowling`

## Ordering
Order books by specific fields:
- `ordering`: Order by `title` or `publication_year` (add `-` for descending order).
Example: `/api/books/?ordering=-publication_year`


# Running API Tests

## Overview
The test suite ensures that all API endpoints for the Book model work as expected, covering:
- CRUD operations.
- Filtering, searching, and ordering functionalities.
- Permissions and authentication enforcement.

## Running Tests
To run the tests, use the following command:
