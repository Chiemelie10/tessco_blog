"""This module defines class CategoryAdminConfig"""
from django.contrib import admin
from category.models import Category


admin.site.register(Category)
