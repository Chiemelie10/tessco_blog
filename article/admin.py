"""This module defines class ArticleAdminConfig"""
from django.contrib import admin
from article.models import Article


admin.site.register(Article)
