from django import template


register = template.Library()


@register.inclusion_tag('googlesearch/inclusion_tags/form.html', takes_context=True)
def googlesearch_form(context):
    #context.update({
    #    'google_search_partner_id': settings.GOOGLE_SEARCH_PARTNER_ID
    #})
    return context


@register.inclusion_tag('googlesearch/inclusion_tags/results.html')
def googlesearch_results():
    return {}
