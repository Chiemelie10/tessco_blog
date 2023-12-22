"""This module defines class DisplayArticleView."""
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from article.models import Article


class DisplayArticleView(View):
    """This class defines methods that handles rendering of an article."""
    def get(self, request, slug_text):
        """This method renders an article on a web page."""
        # pylint: disable=no-member

        try:
            article = Article.objects.get(slug=slug_text)

            author_followers = article.user.followers.all()
            is_following = author_followers.filter(follower=request.user).exists()

            user = request.user
            if user.is_authenticated:
                try:
                    reaction = article.reactions.get(user=user)
                    reaction_value = reaction.reaction_value
                except ObjectDoesNotExist:
                    reaction_value = None
            else:
                reaction_value = None

            return render(request, 'article/display_article.html', {
                'article': article,
                'is_following': is_following,
                'article_reaction': reaction_value
            }, status=200)
        except Article.DoesNotExist:
            return redirect(reverse('page-not-found'))
