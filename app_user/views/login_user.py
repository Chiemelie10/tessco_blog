"""This module defines class LoginUserView"""
from allauth.account.views import LoginView
from django.urls import reverse


class LoginUserView(LoginView):
    """This class subclasses LoginView from allauth."""
    def get_success_url(self):
        return super().get_success_url()
