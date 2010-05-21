from django import template

from options import options

register = template.Library()

@register.inclusion_tag('googlesearch/inclusion_tags/googlesearch_input.html', takes_context=True)
def googlesearch_input(context):
    context.update({
        'options': options.GoogleSearchOptions
    })
    return context

@register.inclusion_tag('googlesearch/inclusion_tags/googlesearch_results.html')
def googlesearch_results():
    return {}
