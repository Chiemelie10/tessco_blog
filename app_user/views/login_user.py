"""This module defines class LoginUserView"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect
from allauth.account.views import LoginView
from app_user.forms import UserModelForm


class LoginUserView(LoginView):
    """This class subclasses LoginView from allauth."""
    form_class = UserModelForm

    def get(self, *args, **kwargs):
        form = self.get_form()
        return render(self.request, 'account/login.html', {'form': form})
    
    def post(self, *args, **kwargs):
        form = self.get_form(self.request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(password)

            user = authenticate(self.request, username=username, password=password)

            if user is not None:
                login(self.request, user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

# class LoginUserView(View):
#     """This class subclasses LoginView from allauth."""
#     def post(self, request):
#         """This method authenticates a user's request to login to the application."""
#         form = UserModelForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             print(password)

#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 home_page = 'app_user/user_home_page.html'
#                 return HttpResponseRedirect(home_page)
#             #else:
#                 #error = "Invalid username or password."

#         return render(request, 'account/login.html', {'form': form})

#     def get(self, request):
#         """This method renders the login page."""
#         form = UserModelForm()
#         return render(request, 'account/login.html', {'form': form})
