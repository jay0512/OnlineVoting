from django import template
import calendar
register = template.Library()

@register.filter
def index(List, i):
    return List[int(i)]

def monthName(List,i):
    return List[int(i)]
