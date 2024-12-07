
from .views import PostSearchView, PostListView
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]


urlpatterns = [
    # Other post-related URLs...
    path('posts/<int:pk>/comments/new/',
         CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/',
         CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/',
         CommentDeleteView.as_view(), name='comment-delete'),
]

urlpatterns = [
    # Other URLs...
    path('tags/<slug:tag_slug>/', PostListView.as_view(), name='posts-by-tag'),
    path('search/', PostSearchView.as_view(), name='post-search'),
]
