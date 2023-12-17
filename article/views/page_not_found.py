"""This module defines PageNotFoundView."""
from django.views import View
from django.shortcuts import render


class PageNotFoundView(View):
    """This class defines a method that render the 404 error page."""
    def get(self, request):
        """This method renders the 404 - Page Not Found error page."""
        return render(request, 'article/404.html', status=404)
