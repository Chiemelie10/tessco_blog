"""This module defines the endpoints of the application related to article_like app."""
from django.urls import path
from article_like.views.article_reaction import ArticleReactionView


urlpatterns = [
    path('api/articles/<slug:slug_text>/like', ArticleReactionView.as_view(),
         name='like-dislike-article'),
    path('api/articles/<slug:slug_text>/like/', ArticleReactionView.as_view(),
         name='like-dislike-article'),
]
