# Create your views here.
from django.http import Http404
from django.template import TemplateDoesNotExist, Context, loader
from django.views.generic.simple import direct_to_template

def education_index(request):
    try:
        return direct_to_template(request, template="education/index.html")
    except TemplateDoesNotExist:
        raise Http404()