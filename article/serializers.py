"""This module defines class ArticleModelSerializer."""
from rest_framework import serializers
from article.models import Article


class ArticleModelSerializer(serializers.ModelSerializer):
    """This class defines the model to serialized"""
    category_name = serializers.CharField(source='category.name')
    class Meta:
        """
            model: Name of the model that will be serialized.
            fields: The fields of the model that will be serialized.
        """
        model = Article
        fields = ['category_name', 'title', 'thumbnail', 'created_at']
