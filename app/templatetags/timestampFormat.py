from django import template
from datetime import datetime
register = template.Library()

@register.filter()
def tchange(value):
    return str(datetime.fromtimestamp(value).__format__('%Y-%m-%d %H:%M'))