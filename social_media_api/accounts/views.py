
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from accounts.serializers import UserSerializer
from accounts.models import CustomUser

# Get the custom user model
CustomUser = get_user_model()

# User Registration View


class UserRegistrationView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    """
    serializer_class = UserSerializer


# User List View (Example for Admin or General Access)
class UserListView(generics.ListAPIView):
    """
    API endpoint for listing all users.
    Only accessible to authenticated users.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# User Detail View
class UserDetailView(generics.RetrieveAPIView):
    """
    API endpoint for retrieving a user's details.
    Only accessible to authenticated users.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# User Login View
class LoginView(APIView):
    """
    API endpoint for user login.
    Returns an authentication token upon successful login.
    """

    def post(self, request, *args, **kwargs):
        from django.contrib.auth import authenticate

        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            if request.user == user_to_follow:
                return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
            request.user.following.add(user_to_follow)
            return Response({"message": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
            if request.user == user_to_unfollow:
                return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
            request.user.following.remove(user_to_unfollow)
            return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
