from django import template
from schedules.models import school_schedule

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_names):
  return user.groups.filter(name__in=group_names).exists()

