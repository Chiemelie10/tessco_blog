"""This module defines the class Article"""
from django.db import models
from django.contrib.auth import get_user_model
from category.models import Category
from image.models import Image


User = get_user_model()

class Article(models.Model):
    """This class defines the columns od the articles table in the database."""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='articles', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='articles', null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_headline = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    thumbnail = models.FileField(upload_to='article-thumbnail')
    images = models.ForeignKey(Image, on_delete=models.SET_NULL,
                               related_name='articles', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """db_table: Name of the table the class creates in the database."""
        db_table = 'articles'

    def __str__(self):
        """This method returns a string representation of the instance of this class."""
        # pylint: disable=no-member
        return f'{self.id}'
