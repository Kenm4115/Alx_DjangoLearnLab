
from .serializers import NotificationSerializer
from .models import Notification
from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from .models import Post, Like
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        followed_users = request.user.following.all()
        posts = Post.objects.filter(
            author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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


class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(
            recipient=request.user).order_by('-timestamp')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Create your views here.
