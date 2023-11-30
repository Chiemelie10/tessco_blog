"""This module defines class LogoutUser"""
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.urls import reverse
from django.http import HttpResponseRedirect


class LogoutUser(LoginRequiredMixin, View):
    """This class defines a method that logout a user."""
    login_url = '/accounts/login'
    redirect_field_name = 'next'

    def get(self, request):
        """This method logs out a user from the application"""
        if request.user.is_authenticated:
            logout(request)
        index_page = request.GET.get('next', reverse('get-index-page'))
        return HttpResponseRedirect(index_page)
