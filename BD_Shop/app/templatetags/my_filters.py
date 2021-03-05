from django import template

register = template.Library()


@register.filter
def create_range(value, start_index=0, step=1):
    return range(start_index, value+start_index, step)


@register.filter
def create_len(arr):
    return len(arr)
