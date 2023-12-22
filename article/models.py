"""This module defines the class Article"""
from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from category.models import Category

User = get_user_model()

PUBLISHED_CHOICES = (
    ('Pending', 'Pending'),
    ('Published', 'Published'),
    ('Rejected', 'Rejected')
)

class Article(models.Model):
    """This class defines the columns od the articles table in the database."""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='articles', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='articles', null=True)
    title = models.CharField(max_length=100)
    content = HTMLField()
    is_headline = models.BooleanField(default=False)
    is_published = models.CharField(max_length=10, choices=PUBLISHED_CHOICES, default='Pending')
    article_is_active = models.BooleanField(default=True)
    thumbnail = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """db_table: Name of the table the class creates in the database."""
        db_table = 'articles'

    def __str__(self):
        """This method returns a string representation of the instance of this class."""
        # pylint: disable=no-member
        return f'{self.id} {self.user} {self.title}'

    def get_total_reactions(self):
        """This method returns the total number of likes and dislikes for an article."""
        # pylint: disable=no-member
        return self.reactions.all().exclude(reaction_value=None).count()

    def get_reaction_type_count(self, reaction_type):
        """This method returns the total number of likes or dislikes for an article."""
        # pylint: disable=no-member
        return self.reactions.filter(reaction_value=reaction_type).count()

    def total_likes(self):
        """This method returns the total number of likes for an article."""
        return self.get_reaction_type_count('like')

    def total_dislikes(self):
        """This method returns the total number of dislikes for an article."""
        return self.get_reaction_type_count('dislike')
