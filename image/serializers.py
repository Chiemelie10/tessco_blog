"""This module defines ImageModelSerializer"""
import mimetypes
from rest_framework import serializers
from image.models import Image


class ImageModelSerializer(serializers.ModelSerializer):
    """This class validates instances of the Image class posted by user."""
    def validate_file(self, value):
        """
        This methods returns a Validation error if image size is more than 1mb
        or mimetype is not one of the accepted ones.
        """
        file_size = value.size

        if file_size > 1000000:
            raise serializers.ValidationError('Image size exceeds the allowed limit of 1mb')
        
        allowed_mimetypes = [
            'image/jpeg', 'image/jpg', 'image/png',
            'image/webp', 'image/jpe', 'image/jfi',
            'image/jif', 'image/jfif'
        ]

        image_mimetype = mimetypes.guess_type(value.name)

        if image_mimetype[0] not in allowed_mimetypes:
            raise serializers.ValidationError('Invalid file type')

        return value
    class Meta:
        """
            model: Name of the model that will be serialized.
            fields: The fields of the model that will be validated.
        """
        model = Image
        fields = ['file']
