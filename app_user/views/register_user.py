"""This module defines class RegisterUser"""
from django.shortcuts import render
from django.views import View
from app_user.forms import UserModelForm


class RegisterUser(View):
    """This module defines a post method for registering a new user"""
    def post(self, request):
        """This method adds a new user to the database"""
        form = UserModelForm(request.POST)
