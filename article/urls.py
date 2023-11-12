"""This module defines the endpoints of the app related to articles."""
from django.urls import path
from article.views.index_page_api import IndexPageApi
from article.views.index_page_headline_api import IndexPageHeadline


urlpatterns = [
    path('api/articles/', IndexPageApi.as_view(), name='get-active-articles-api'),
    path('api/articles', IndexPageApi.as_view(), name='get-active-articles-api'),
    path('api/articles/headlines/', IndexPageHeadline.as_view(), name='get-active-headline'),
    path('api/articles/headlines', IndexPageHeadline.as_view(), name='get-active-headline')
]
