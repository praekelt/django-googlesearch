from django import template

from preferences import preferences

register = template.Library()

@register.inclusion_tag('googlesearch/inclusion_tags/googlesearch_input.html', takes_context=True)
def googlesearch_input(context):
    return context

@register.inclusion_tag('googlesearch/inclusion_tags/googlesearch_results.html')
def googlesearch_results():
    return {}
