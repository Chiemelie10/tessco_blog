"""This module defines class image."""
from django.db import models


class Image(models.Model):
    """This class defines the columns of the images table in the database."""
    image = models.FileField(upload_to='article_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """db_table: Name of the table this class creates in the database."""
        db_table = 'images'

    def __str__(self):
        """This method returns a string representation of the instance of this class."""
        # pylint: disable=no-member
        return f'{self.id}'
