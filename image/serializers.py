"""This module defines ImageModelSerializer"""
from rest_framework import serializers
from image.models import Image


class ImageModelSerializer(serializers.ModelSerializer):
    """This class validates instances of the Image class posted by user."""
    class Meta:
        """
            model: Name of the model that will be serialized.
            fields: The fields of the model that will be validated.
        """
        model = Image
        fields = ['file']
