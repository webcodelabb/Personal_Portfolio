from django import template

register = template.Library()

@register.filter
def to(value, arg):
    try:
        start = int(value)
        end = int(arg)
        return range(start, end + 1)  # Include the end value
    except ValueError:
        return []



@register.filter
def range_filter(value):
    """
    Converts a number into a range object to be used in templates for iteration.
    """
    try:
        return range(int(value))
    except (ValueError, TypeError):
        return []
