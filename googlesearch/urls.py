import django
version = django.get_version()

if version < 1.6:
    from django.conf.urls.default import patterns, url
else:
    from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',

    url(
        r'^results/$', 
        'django.views.generic.simple.direct_to_template', 
        {'template': 'googlesearch/results.html'},
        name='googlesearch-results'
    ),

    url(
        r'^cref-cse\.xml/$', 
        'googlesearch.views.cref_cse', 
        {},
        name='googlesearch-cref-cse'
    ),
)
