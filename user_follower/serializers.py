"""This module defines the UserFollowForm"""
from rest_framework import serializers
from user_follower.models import UserFollow


class UserFollowForm(serializers.ModelSerializer):
    """
    This class defines the fields of the UserFollow
    class that will be validated.
    """
    class Meta:
        """
            model: Name of the model
            fields: Fields that will be validated.
        """
        model = UserFollow
        fields = '__all__'
