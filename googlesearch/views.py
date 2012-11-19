from django.http import HttpResponse
from django.template import RequestContext, loader


def cref_cse(request):
    return HttpResponse(
        loader.render_to_string('googlesearch/cref_cse.xml', {}, context_instance=RequestContext(request)),
        mimetype = 'text/xml'
    )
