Django Google Search
====================
**Django Google custom search engine app.**

Provides a simple tag rendering a Google Custom Search Engine input field and a view displaying search results.

.. contents:: Contents
    :depth: 5

Installation
------------

#. Install or add ``django-googlesearch`` to your Python path.

#. Add ``googlesearch`` to your ``INSTALLED_APPS`` setting.

#. Add a ``GOOGLE_SEARCH_PARTNER_ID`` setting to your project's ``settings.py`` file. This setting specifies the Google Custom Search Engine ID to use when rendering the Google search box, as provided by Google, i.e.::

    GOOGLE_SEARCH_PARTNER_ID = 'partner-pub-329847239847234:xcvx-3kasd'

#. Add googlesearch url include to your project's ``urls.py`` file::

    (r'^search/', include('googlesearch.urls')),

#. Optionally add ``"django.core.context_processors.request",`` to your ``TEMPLATE_CONTEXT_PROCESSORS`` setting, i.e.::

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.core.context_processors.request",
        ...other processors...
    )


