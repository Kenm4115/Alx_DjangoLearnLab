
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book



class BookAPITestCase(APITestCase):
     """
    Test suite for Book API endpoints.
    This suite tests:
    - CRUD operations (create, retrieve, update, delete).
    - Advanced query capabilities (filtering, searching, ordering).
    - Authentication and permission handling.
    """
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create test data
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter 1", publication_year=1997, author=self.author)
        self.book2 = Book.objects.create(title="Harry Potter 2", publication_year=1998, author=self.author)
        
        self.create_url = '/api/books/create/'
        self.list_url = '/api/books/'
        self.detail_url = f'/api/books/{self.book1.id}/'
        self.update_url = f'/api/books/{self.book1.id}/update/'
        self.delete_url = f'/api/books/{self.book1.id}/delete/'

    # Test: List all books
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Test: Retrieve a book by ID
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter 1")

    # Test: Create a book
    def test_create_book(self):
        data = {
            "title": "Harry Potter 3",
            "publication_year": 1999,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # Test: Update a book
    def test_update_book(self):
        data = {
            "title": "Updated Harry Potter",
            "publication_year": 2000,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Harry Potter")

    # Test: Delete a book
    def test_delete_book(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # Test: Filtering books by title
    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url + '?title=Harry Potter 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter 1")

    # Test: Search books
    def test_search_books(self):
        response = self.client.get(self.list_url + '?search=Rowling')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Test: Ordering books by publication year
    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1997)
        self.assertEqual(response.data[1]['publication_year'], 1998)

    # Test: Unauthenticated user access to restricted endpoints
    def test_unauthenticated_user_restricted_access(self):
        self.client.logout()
        response = self.client.post(self.create_url, {
            "title": "Harry Potter 4",
            "publication_year": 2001,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
