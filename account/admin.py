"""This module defines class BankDetailsAdminConfig"""
from django.contrib import admin
from account.models import BankDetail


admin.site.register(BankDetail)
