
from posts.views import FeedView, PostListCreateView, PostDetailView
from .views import LikePostView, UnlikePostView, FeedView, CommentViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'posts', basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls


urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
