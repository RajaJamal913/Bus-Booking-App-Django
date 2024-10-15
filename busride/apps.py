from django.apps import AppConfig


class BusrideConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'busride'

from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})
