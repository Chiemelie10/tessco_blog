"""This module defines class ArticleReactionView"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from article_like.models import ArticleReaction
from article.models import Article


class ArticleReactionView(APIView):
    """This class defines a post method that handles like and dislike reactions."""

    def post(self, request, slug_text):
        """This method saves value of user reation to an article in the database."""
        # pylint: disable=no-member

        data = request.data
        user = request.user

        if not user.is_authenticated:
            redirect_return_path = data.get('pathname')
            current_site = get_current_site(request)

            if str(current_site) == 'http://127.0.0.1:8000':
                current_site = 'http://localhost:8000'

            login_url = f"{current_site}{reverse('account_login')}"\
                        f"?next={redirect_return_path}"

            return redirect(login_url)

        try:
            article = Article.objects.get(slug=slug_text)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found.'},
                            status=status.HTTP_404_NOT_FOUND)

        reaction_value = data.get('reaction')

        if reaction_value is None:
            return Response({'error': 'Reaction value is required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        if reaction_value != 'like' and reaction_value != 'dislike':
            return Response({'error': 'Reaction value must be like or dislike.'},
                            status=status.HTTP_400_BAD_REQUEST)

        reaction_obj, created = ArticleReaction.objects.get_or_create(user=user,
                                                                      article=article)

        if created:
            reaction_obj.reaction_value = reaction_value
            reaction_obj.save()

            data = {
                'message': 'Reaction saved successfully.',
                'reaction': reaction_value,
                'total_likes': article.total_likes(),
                'total_dislikes': article.total_dislikes()
            }

            return Response(data, status=status.HTTP_200_OK)

        if reaction_value == 'like' and reaction_obj.reaction_value == 'like':
            reaction_obj.reaction_value = None
            reaction_obj.save()

            data = {
                'message': 'Reaction saved successfully.',
                'reaction': 'null',
                'total_likes': article.total_likes(),
                'total_dislikes': article.total_dislikes()
            }

            return Response(data, status=status.HTTP_200_OK)

        if reaction_value == 'like' and reaction_obj.reaction_value == 'dislike':
            reaction_obj.reaction_value = reaction_value
            reaction_obj.save()

            data = {
                'message': 'Reaction saved successfully.',
                'reaction': reaction_value,
                'total_likes': article.total_likes(),
                'total_dislikes': article.total_dislikes()
            }

            return Response(data, status=status.HTTP_200_OK)

        if reaction_value == 'like' and reaction_obj.reaction_value is None:
            reaction_obj.reaction_value = reaction_value
            reaction_obj.save()

            data = {
                'message': 'Reaction saved successfully.',
                'reaction': reaction_value,
                'total_likes': article.total_likes(),
                'total_dislikes': article.total_dislikes()
            }

            return Response(data, status=status.HTTP_200_OK)

        if reaction_value == 'dislike' and reaction_obj.reaction_value == 'dislike':
            reaction_obj.reaction_value = None
            reaction_obj.save()

            data = {
                'message': 'Reaction saved successfully.',
                'reaction': 'null',
                'total_likes': article.total_likes(),
                'total_dislikes': article.total_dislikes()
            }

            return Response(data, status=status.HTTP_200_OK)

        if reaction_value == 'dislike' and reaction_obj.reaction_value == 'like':
            reaction_obj.reaction_value = reaction_value
            reaction_obj.save()

            data = {
                'message': 'Reaction saved successfully.',
                'reaction': reaction_value,
                'total_likes': article.total_likes(),
                'total_dislikes': article.total_dislikes()
            }

            return Response(data, status=status.HTTP_200_OK)

        if reaction_value == 'dislike' and reaction_obj.reaction_value is None:
            reaction_obj.reaction_value = reaction_value
            reaction_obj.save()

            data = {
                'message': 'Reaction saved successfully.',
                'reaction': reaction_value,
                'total_likes': article.total_likes(),
                'total_dislikes': article.total_dislikes()
            }

            return Response(data, status=status.HTTP_200_OK)
