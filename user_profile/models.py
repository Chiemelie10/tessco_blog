"""This module defines class UserProfile"""
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from role.models import Role
from category.models import Category


User = get_user_model()

class UserProfile(models.Model):
    """This class defines the columns of the content_creators table."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True,
                                related_name='user_profile', primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    phone_number = models.CharField(max_length=11, unique=True,
                                    validators=[MinLengthValidator(limit_value=11)])
    thumbnail = models.FileField(upload_to='thumbnail')
    cv = models.FileField(upload_to='cv', blank=True, null=True)
    role = models.OneToOneField(Role, on_delete=models.SET_NULL,
                                null=True, related_name='user_profile')
    category = models.OneToOneField(Category, on_delete=models.SET_NULL,
                                    null=True, related_name='user_profile')
    is_approved = models.BooleanField(default=False)
    level = models.IntegerField(default=0, validators=[MinValueValidator(limit_value=0),
                                                       MaxValueValidator(limit_value=10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
