from django import template

register = template.Library()


@register.filter
def mul(value, arg):
    """Multiply the value by the argument."""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return 0


@register.filter
def div(value, arg):
    """Divide the value by the argument."""
    try:
        result = int(value) / int(arg)
        return int(result)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0


@register.filter
def format_number(value):
    """Format a number with commas."""
    try:
        return f"{int(value):,}"
    except (ValueError, TypeError):
        return value