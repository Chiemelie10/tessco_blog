"""This module defines class IndexPage"""
# from django.shortcuts import render
from django.views.generic.list import ListView
from article.models import Article
from category.models import Category


class IndexPage(ListView):
    """This class defines a method that renders the index page."""
    # def get(self, request):
    #     """
    #         Args:
    #             request: The request object
    #         Return:
    #             Renders the titles of all articles in the database.
    #     """
    #     # pylint: disable=no-member

    #     articles = Article.objects.filter(is_active=True).order_by('-created_at')
    #     return render(request, 'app_user/index.html', {
    #         'articles': articles
    #     }, status=200)

    # pylint: disable=no-member

    model = Article
    paginate_by = 8
    context_object_name = 'articles'
    template_name = 'app_user/index.html'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        """This method adds more context to context_object_name."""
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
