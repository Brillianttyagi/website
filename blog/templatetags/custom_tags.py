from django import template

register = template.Library()

@register.filter
def remove_spaces(value):
    return value.replace('_', ' ')
@register.filter
def to_str(value):
    """converts int to string"""
    return str(value)

@register.filter
def firstone(value):
    """converts int to string"""
    return value[0]

@register.filter
def des(value):
    """converts int to string"""
    li = value.split("</p>")
    return li[0][3:]
