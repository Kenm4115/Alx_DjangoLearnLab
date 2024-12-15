
from accounts.views import UserRegistrationView, UserListView, UserDetailView, LoginView
from django.urls import path
from .views import LoginView, FollowUserView, UnfollowUserView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/',
         UnfollowUserView.as_view(), name='unfollow_user'),
]
