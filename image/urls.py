"""This module defines url endpoints handled by the application."""
from django.urls import path
from image.views.article_images import ImageUploadView


urlpatterns = [
    path('api/images', ImageUploadView.as_view(), name='upload-image'),
    path('api/images/', ImageUploadView.as_view(), name='upload-image'),
]
