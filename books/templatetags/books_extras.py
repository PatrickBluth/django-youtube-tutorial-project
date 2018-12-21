from django import template

from books import models

register = template.Library()


@register.simple_tag
def all_genres(start_char):
    return models.Genre.objects.filter(topic__startswith=start_char)


@register.filter
def read_time_estimate(page_length):
    return round(page_length/100, 1)
