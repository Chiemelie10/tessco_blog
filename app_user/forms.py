"""This module defines class UserModelForm and UserProfileForm"""
from django import forms
from django.contrib.auth import get_user_model
from user_profile.models import UserProfile


User = get_user_model()

class UserModelForm(forms.ModelForm):
    """This class defines fields of the model to be validated"""
    class Meta:
        """
        model: Name of the model
        fields: The fields of the model that will be validated through the form
        """
        model = User
        fields = ['username', 'email', 'password']


class UserProfileForm(forms.ModelForm):
    """This class defines fields of the model to be validated"""
    class Meta:
        """
        model: Name of the model
        fields: The fields of the model that will be validated through the form
        """
        model = UserProfile
        fields = ['user', 'first_name', 'last_name', 'bio', 'phone_number',
                  'thumbnail', 'role', 'category']
