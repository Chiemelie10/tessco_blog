"""This module defines the function most_significant_timeunit."""
from django import template
from django.utils.timesince import timesince


register = template.Library()

@register.filter
def most_significant_timeunit(date_value):
    """Returns the fisrt time unit from timesince"""
    time_since = timesince(date_value)
    significant_date_unit = time_since.split(", ")
    if significant_date_unit:
        return significant_date_unit[0]
    return ""
