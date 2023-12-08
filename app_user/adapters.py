"""This module defines CustomAccountAdapter."""
from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    """This class overides the allauth DefaultAccountAdapter"""
    def get_login_redirect_url(self, request):
        """
        If next in url query string, this method returns the value.
        Otherwise it returns the the value provided by the super class.
        """
        next_page = request.GET.get("next")
        print(next_page)
        if next_page is not None:
            return next_page
        return super().get_login_redirect_url(request)
