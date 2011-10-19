from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404

def home(request):
    page_title = "Development Testing"
    return render(request, 'index.html', locals())
