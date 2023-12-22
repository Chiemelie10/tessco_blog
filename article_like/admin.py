"""This module defines the configuration settings of the article_like app in the admin page."""
from django.contrib import admin
from article_like.models import ArticleReaction

admin.site.register(ArticleReaction)
