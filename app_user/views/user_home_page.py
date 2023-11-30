"""This module defines class UserHomePage."""
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from article.models import Article
from category.models import Category


class UserHomePage(LoginRequiredMixin, ListView):
    """This class renders user's home page."""
    # pylint: disable=no-member

    login_url = '/accounts/login'
    redirect_field_name = 'next'
    model = Article
    context_object_name = 'articles'
    paginate_by = 8
    template_name = 'app_user/user_home_page.html'

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
