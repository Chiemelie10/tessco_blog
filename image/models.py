"""This module defines class image."""
from django_resized import ResizedImageField
from django.db import models
from django.contrib.auth import get_user_model
from article.models import Article


User = get_user_model()
class Image(models.Model):
    """This class defines the columns of the images table in the database."""
    file = models.ImageField(upload_to='article_images', null=True)
    image_300w = ResizedImageField(size=[300, None], upload_to='article_image_300w', quality=100, blank=True)
    image_600w = ResizedImageField(size=[600, None], upload_to='article_image_600w', quality=100, blank=True)
    image_900w = ResizedImageField(size=[900, None], upload_to='article_image_900w', quality=100, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """db_table: Name of the table this class creates in the database."""
        db_table = 'images'

    def __str__(self):
        """This method returns a string representation of the instance of this class."""
        # pylint: disable=no-member
        return f'{self.id}'
