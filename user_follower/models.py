"""This module defines class Follow"""
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class UserFollow(models.Model):
    """This class defines the attributes of the UserFollower class."""
    # user that made request to follow another user
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following', editable=False)
    # User that will be followed by the user that made the request
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers', editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """db_table: Name of the table this class creates in the database."""
        db_table = 'user_follows'

    def __str__(self):
        """This method returns a string representation of the instance of this class."""
        # pylint: disable=no-member
        return f'Follower: {self.follower} - Following: {self.following}'
