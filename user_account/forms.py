"""This module defines class UserModelForm and UserProfileForm"""
from django import forms
from account.models import BankDetails


class BankDetailsForm(forms.ModelForm):
    """This class defines fields of the model to be validated"""
    class Meta:
        """
        model: Name of the model
        fields: The fields of the model that will be validated through the form
        """
        model = BankDetails
        fields = ['bank_name', 'account_number']
