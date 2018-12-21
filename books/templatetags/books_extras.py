from django import template

from books import models

register = template.Library()


@register.simple_tag
def all_genres(start_char):
    return models.Genre.objects.filter(topic__startswith=start_char)
