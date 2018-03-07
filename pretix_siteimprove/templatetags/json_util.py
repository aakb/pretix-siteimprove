import json

from django import template

register = template.Library()


@register.filter(name='json_encode')
def json_encode(value, arg=None):
    return json.dumps(value)
