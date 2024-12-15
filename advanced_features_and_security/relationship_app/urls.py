from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.contrib import admin
from .views import add_book, edit_book, delete_book
from .views import admin_view, librarian_view, member_view
from .views import register
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import list_books, LibraryDetailView, AddBookView, EditBookView


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('add_book/', AddBookView.as_view(), name='add_book'),
    path('edit_book/<int:pk>/', EditBookView.as_view(), name='edit_book'),
]


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='relationship_app/logged_out.html'), name='logout'),
]


urlpatterns = [
    path('admin_dashboard/', admin_view, name='admin_dashboard'),
    path('librarian_dashboard/', librarian_view, name='librarian_dashboard'),
    path('member_dashboard/', member_view, name='member_dashboard'),
]


urlpatterns = [
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),
]


urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
