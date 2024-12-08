
from .views import (
    add_comment, CommentUpdateView,
    CommentDeleteView
)
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/logged_out.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/comments/new/', add_comment, name='comment-add'),
    path('comments/<int:pk>/edit/',
         CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/',
         CommentDeleteView.as_view(), name='comment-delete'),
]


# urlpatterns = [
#     path('', PostListView.as_view(), name='post-list'),
#     path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
#     path('posts/new/', PostCreateView.as_view(), name='post-create'),
#     path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
#     path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
# ]


# urlpatterns = [
#     # ... existing patterns
#     path('posts/<int:post_id>/comments/new/', add_comment, name='comment-add'),
#     path('comments/<int:pk>/edit/',
#          CommentUpdateView.as_view(), name='comment-update'),
#     path('comments/<int:pk>/delete/',
#          CommentDeleteView.as_view(), name='comment-delete'),
# ]
