"""This module defines class DisplayArticleView."""
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from article.models import Article


class DisplayArticleView(View):
    """This class defines methods that handles rendering of an article."""
    def get(self, request, slug_text):
        """This method renders an article on a web page."""
        # pylint: disable=no-member
        # pylint: disable=unused-argument
        try:
            article = Article.objects.get(slug=slug_text)
            return render(request, 'article/display_article.html', {
                'article': article
            }, status=200)
        except Article.DoesNotExist:
            return redirect(reverse('page-not-found'))
