"""This module defines the endpoints of the application related to user_follower app."""
from django.urls import path
from user_follower.views.user_follow import UserFollowView


urlpatterns = [
    path('api/users/follow', UserFollowView.as_view(), name='follow-unfollow-user'),
    path('api/users/follow/', UserFollowView.as_view(), name='follow-unfollow-user'),
]
