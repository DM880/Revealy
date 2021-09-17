from django import template
from chats.models import *

register = template.Library()

@register.inclusion_tag('chat_base.html')
def get_chats_objects(queryset, **filters):
    if not filters:
        raise template.TemplateSyntaxError('`get_chats_objects` tag requires filters.')
    return queryset.filter(**filters).first()