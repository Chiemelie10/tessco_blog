"""This module defines class UserProfile"""
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from role.models import Role


User = get_user_model()

APPROVED_CHOICES = (
    ('Pending', 'Pending'),
    ('Published', 'Published'),
    ('Rejected', 'Rejected')
)

class UserProfile(models.Model):
    """This class defines the columns of the content_creators table."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True,
                                related_name='user_profile', primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=11, unique=True,
                                    validators=[MinLengthValidator(limit_value=11)])
    thumbnail = models.FileField(upload_to='thumbnail', blank=True, null=True)
    role = models.OneToOneField(Role, on_delete=models.SET_NULL,
                                null=True, related_name='user_profile')
    is_approved = models.CharField(max_length=10, default='Pending', choices=APPROVED_CHOICES)
    level = models.IntegerField(default=0, validators=[MinValueValidator(limit_value=0),
                                                       MaxValueValidator(limit_value=10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
