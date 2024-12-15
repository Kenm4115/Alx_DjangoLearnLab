
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

    def get(self, request):
        # Get the current user
        current_user = request.user

        # Get the list of users that the current user follows
        following_users = current_user.following.all()

        # Query posts created by these users, ordered by creation date (newest first)
        Post.objects.filter(
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


# class FeedView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         followed_users = request.user.following.all()
#         posts = Post.objects.filter(
#             author__in=followed_users).order_by('-created_at')
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            like, created = Like.objects.get_or_create(
                user=request.user, post=post)

            if created:
                # Create a notification for the post author
                if post.author != request.user:
                    Notification.objects.create(
                        recipient=post.author,
                        actor=request.user,
                        verb="liked your post",
                        target=post
                    )
                return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)
            return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)


class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            like = Like.objects.filter(user=request.user, post=post)
            if like.exists():
                like.delete()
                return Response({"message": "Post unliked."}, status=status.HTTP_200_OK)
            return Response({"message": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)



