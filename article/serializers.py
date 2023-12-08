"""This module defines class ArticleModelSerializer."""
from rest_framework import serializers
from django.core.validators import MaxLengthValidator
from article.models import Article


class IndexPageSerializer(serializers.ModelSerializer):
    """This class defines the fields of the article class that will be returned."""
    category_name = serializers.CharField(source='category.name')
    class Meta:
        """
            model: Name of the model that will be serialized.
            fields: The fields of the model that will be serialized.
        """
        model = Article
        fields = ['category_name', 'title', 'thumbnail', 'created_at']


class SubmitArticleSerializer(serializers.ModelSerializer):
    """This class validates instances of the Article class posted by users."""
    content = serializers.CharField(validators=[MaxLengthValidator(20)], required=True)
    class Meta:
        """
            model: Name of the model that will be serialized.
            fields: The fields of the model that will be validated.
        """
        model = Article
        fields = "__all__"
