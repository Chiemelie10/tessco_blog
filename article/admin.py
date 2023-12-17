"""This module defines class ArticleAdminConfig"""
from uuid import uuid4
from django.contrib import admin
from django.utils.text import slugify
from article.models import Article


class ArticleAdmin(admin.ModelAdmin):
    """This class configures the Article model admin"""
    search_fields = ('id', 'user', 'title', 'category')
    ordering = ('created_at',)
    list_filter = ('is_published', 'is_headline')
    list_display = ('id', 'user', 'title', 'is_headline', 'is_published')

    def save_model(self, request, obj, form, change):
        """
        This save method was overriden to populate the slug field
        with the value of the title field. It appends a unique number only to
        the title for the slug field if the title already exists.
        """
        slug = slugify(obj.title)

        # Ensure the slug is unique
        articles = Article.objects.filter(slug=slug) # pylint: disable=no-member

        if articles.exists():
            base_slug = slug
            unique_id = str(uuid4())[:8]
            slug = f"{base_slug}-{unique_id}"

        obj.slug = slug

        return super().save_model(request, obj, form, change)

admin.site.register(Article, ArticleAdmin)
