"""This module defines ArticleComment"""
from django.db import models
from django.contrib.auth import get_user_model
from article.models import Article


User = get_user_model()

class ArticleComment(models.Model):
    """
    This class defines the columns that will be
    created in article_likes table in the database.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    parent_comment = models.ForeignKey('self', null=True, blank=True,
                                       on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """db_table: Name of the table this class creates in the database."""
        db_table = 'comments'

    def __str__(self):
        """This method returns a string representation of the instance of this class."""
        # pylint: disable=no-member
        return f'{self.user.username} commented: {self.text}'
