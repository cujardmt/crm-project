from django import template

register = template.Library()

@register.filter
def getattribute(instance, field_name):
    if hasattr(instance, field_name):
        return getattr(instance, field_name)
    return None
