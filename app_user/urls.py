"""This module defines the endpoints of the tessco blog app."""
from django.urls import path
from app_user.views.index_page import IndexPage
# from app_user.views.user_home_page import UserHomePage
#from app_user.views.logout_user import LogoutUser


urlpatterns = [
    path('', IndexPage.as_view(), name='get-home-page'),
    # path('home/', UserHomePage.as_view(), name='get-home-page'),
    # path('logout/', LogoutUser.as_view(), name='logout'),
]
