from django.conf.urls.defaults import patterns, url

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
        'django.views.generic.simple.direct_to_template', 
        {'template': 'googlesearch/cref_cse.xml'},
        name='googlesearch-cref-cse'
    ),
)
