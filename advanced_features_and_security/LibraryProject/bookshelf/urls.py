
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('books/', views.book_list, name='book_list'),
    path('add-book/', views.add_book, name='add_book'),
]

