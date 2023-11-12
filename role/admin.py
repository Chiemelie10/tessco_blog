"""This module defines class RoleAdminConfig"""
from django.contrib import admin
from role.models import Role


admin.site.register(Role)
