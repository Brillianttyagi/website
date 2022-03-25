from django import template

register = template.Library()

@register.filter
def return_first(value,arg):
    """converts int to string"""
    return value[arg]