from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'django.views.generic.simple',
    url(r'^results/$', 'direct_to_template', {'template': \
            'googlesearch/googlesearch_results.html', 'extra_context': \
            {'title': 'Search Results'}}, name='googlesearch_results'),
)
