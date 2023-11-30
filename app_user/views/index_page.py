"""This module defines class IndexPage"""
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from article.models import Article
from category.models import Category


class IndexPage(ListView):
    """This class defines a method that renders the index page."""
    # pylint: disable=no-member

    model = Article
    paginate_by = 8
    context_object_name = 'articles'
    template_name = 'app_user/index.html'

    def get_queryset(self):
        """This method returns articles that are active."""
        return Article.objects.filter(article_is_active=True).order_by('-created_at')

    def get_context_data(self, **kwargs):
        """This method adds more context to context_object_name."""
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.get_queryset(), self.paginate_by)
        total_pages = paginator.num_pages

        context['total_pages'] = total_pages
        context['categories'] = Category.objects.all()
        return context
