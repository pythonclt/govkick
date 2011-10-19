from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, Context

def home(request):
    page_title = "Development Testing"
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))
