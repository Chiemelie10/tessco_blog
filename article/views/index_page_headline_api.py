"""This module defines class IndexPageHeadline."""
from rest_framework.views import APIView
from django.http import JsonResponse
from article.models import Article
from article.serializers import IndexPageSerializer


class IndexPageHeadline(APIView):
    """
    This class defines a method that returns all active
    articles that are headlines.
    """
    # pylint: disable=no-member
    # pylint: disable=unused-argument

    def get(self, request):
        """This method returns all active articles that have headline set to true"""
        headlines = Article.objects.filter(article_is_active=True, is_headline=True).order_by('-created_at')
        serializer = IndexPageSerializer(headlines, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
