
from rest_framework import generics, permissions, status, viewsets, filters
from notifications.models import Notification
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from posts.models import Post, Like, Comment
from posts.serializers import PostSerializer, CommentSerializer


class FeedView(APIView):
    """
    API endpoint to display posts from users the authenticated user follows.
    """
    permission_classes = [permissions.IsAuthenticated]

    Post.objects.filter(author__in=following_users).order_by

    def get(self, request):
        # Get the current user
        current_user = request.user

        # Get the list of users that the current user follows
        following_users = current_user.following.all()

        # Query posts created by these users, ordered by creation date (newest first)
        posts = Post.objects.filter(
            author__in=following_users).order_by('-created_at')

        # Serialize the posts and return them
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Post List/Create View


class PostListCreateView(generics.ListCreateAPIView):
    """
    API view to list all posts or create a new post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Post Detail View
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a single post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs.get("pk"))


# Like and Unlike Post View
class LikePostView(APIView):
    """
    API endpoint to like or unlike a post.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # Ensure the post exists
        like, created = Like.objects.get_or_create(
            user=request.user, post=post)

        if created:
            return Response({"message": "Post liked successfully!"}, status=status.HTTP_201_CREATED)
        else:
            like.delete()
            return Response({"message": "Post unliked successfully!"}, status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikePostView(APIView):
    """
    API endpoint to like a post.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Retrieve the post object
        post = get_object_or_404(Post, pk=pk)

        # Create a like if it doesn't exist; otherwise, retrieve it
        like, created = Like.objects.get_or_create(
            user=request.user, post=post)

        if created:
            return Response({'message': 'Post liked successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'You have already liked this post!'}, status=status.HTTP_400_BAD_REQUEST)


class UnlikePostView(APIView):
    """
    API endpoint to unlike a post.
    """
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        # Retrieve the post object
        post = get_object_or_404(Post, pk=pk)

        # Try to find and delete the like
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'message': 'Post unliked successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'message': 'You have not liked this post!'}, status=status.HTTP_400_BAD_REQUEST)
