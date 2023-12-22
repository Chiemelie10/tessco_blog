"""This module defines ArticleReaction"""
from django.db import models
from django.contrib.auth import get_user_model
from article.models import Article


User = get_user_model()

REACTION_VALUE_CHOICES = (
    ('like', 'Like'),
    ('dislike', 'Dislike')
)

class ArticleReaction(models.Model):
    """
    This class defines the columns that will be
    created in article_likes table in the database.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reactions')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reactions')
    reaction_value = models.CharField(max_length=10, choices=REACTION_VALUE_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """db_table: Name of the table this class creates in the database."""
        db_table = 'article_reactions'

    def __str__(self):
        """This method returns a string representation of the instance of this class."""
        # pylint: disable=no-member
        return f'{self.user.username} - {self.article.title} - {self.reaction_value}'
