Django Google Search
====================
**Django Google custom search engine app.**

Provides a simple tag rendering a Google Custom Search Engine input field and a view displaying search results. 
The product is an implementation of http://www.google.com/cse/docs/cref.html. The custom search engine definition 
is stored on your site, not by Google. This allows you to define a search engine in version controlled code.

.. contents:: Contents
    :depth: 5

Installation
------------

#. Install or add ``django-googlesearch`` to your Python path.

#. Add ``googlesearch`` to your ``INSTALLED_APPS`` setting.

#. Add googlesearch url include to your project's ``urls.py`` file::

    (r'^search/', include('googlesearch.urls')),

#. Optionally add ``"django.core.context_processors.request",`` to your ``TEMPLATE_CONTEXT_PROCESSORS`` setting, i.e.::

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.core.context_processors.request",
        ...other processors...
    )

   We need a ``request`` object when rendering the search input field and results to be able to display the search query value. This is optional and is not required for operation but is highly recommended. 

Usage
-----

Once installed you can add a Google search box to your templates by using the ``googlesearch_form`` template tag, i.e.::

    {% load googlesearch_inclusion_tags %}
    
    ...some html...
    
    {% googlesearch_form %}
    
    ...some more html...

By default search results are displayed through the view with URL named ``googlesearch-results``, as defined in ``googlesearch.urls``.
You can create your own URL named ``googlesearch-results`` and include the ``googlesearch_results`` template tag in its template to display results, i.e.::

    {% load googlesearch_inclusion_tags %}
    
    ...some html...
    
    {% googlesearch_results %}
    
    ...some more html...

