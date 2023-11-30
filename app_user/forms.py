"""This module defines class UserModelForm and UserProfileForm"""
from django import forms
from django.contrib.auth import get_user_model, authenticate
from allauth.account.forms import LoginForm
from user_profile.models import UserProfile


User = get_user_model()

class UserModelForm(LoginForm):
    """This class defines fields of the model to be validated"""

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(UserModelForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(label='Username', max_length=100, required=True)
        self.fields['username'].widget.attrs['autocomplete'] = 'username'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        # self.fields['password'].widget = forms.PasswordInput(attrs={'type': 'password'})
        # self.fields['password'].widget = forms.PasswordInput(attrs={'autocomplete': 'current-password'})

    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get('username', 'tessco')
    #     password = cleaned_data.get('password')

    #     user = self.authenticate(self.request, username=username, password=password)

    #     if user is None:
    #         raise forms.ValidationError('Invalid username or password.')
        
    #     return cleaned_data

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
