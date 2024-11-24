
from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Map to /books/ endpoint
    path('', include(router.urls)),  # Include the router-generated URLs
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),  # Token login endpoint
]





