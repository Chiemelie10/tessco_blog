"""This module defines ArticleLike"""
from django.db import models
from django.contrib.auth import get_user_model
from article.models import Article


User = get_user_model()

class ArticleLike(models.Model):
    """
    This class defines the columns that will be
    created in article_likes table in the database.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """db_table: Name of the table this class creates in the database."""
        db_table = 'likes'

    def __str__(self):
        """This method returns a string representation of the instance of this class."""
        # pylint: disable=no-member
        return f'{self.user}'
