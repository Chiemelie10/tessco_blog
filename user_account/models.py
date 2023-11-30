"""This model defines class BankDetails"""
from django.db import models
from django.core.validators import MinLengthValidator
from user_profile.models import UserProfile


class BankDetail(models.Model):
    """This class defines the columns of the bank_details table in the database."""
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE,
                                primary_key=True, related_name='bank_detail')
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=10,
                                      validators=[MinLengthValidator(limit_value=10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """db_table: Name of the table this class creates in the database."""
        db_table = 'bank_details'

    def __str__(self):
        """This method returns a string representation of the instance of this class."""
        return f'{self.user}'
