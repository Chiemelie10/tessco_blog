"""This module defines class ImageAdminConfig"""
from django.contrib import admin
from image.models import Image


admin.site.register(Image)
