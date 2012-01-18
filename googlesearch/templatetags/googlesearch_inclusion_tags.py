from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('googlesearch/inclusion_tags/googlesearch_input.html', takes_context=True)
def googlesearch_input(context):
    context.update({
        'google_search_partner_id': settings.GOOGLE_SEARCH_PARTNER_ID
    })
    return context


@register.inclusion_tag('googlesearch/inclusion_tags/googlesearch_results.html')
def googlesearch_results():
    return {}
