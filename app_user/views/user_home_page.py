"""This module defines class UserHomePage."""
from django.views.generic.list import ListView
from article.models import Article
from category.models import Category


class UserHomePage(ListView):
    """This class renders user's home page."""
    model = Article
    context_object_name = 'articles'
    paginate_by = 8
    template_name = 'app_user/user_home_page.html'
    ordering = '-created_at'

    def get_context_data(self, **kwargs):
        """This method adds more context to context_object_name."""
        # pylint: disable=no-member
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
