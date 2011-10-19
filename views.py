from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404

def home(request):
    ### START html header variables ###
    page_title = "Home"
    meta_keywords = "Govkick, government, home, signup, sign-up"
    meta_description = "Home page for Govkick.com"
    ### END html header variables ###

    random_message = "Development testing"
    return render(request, 'index.html', locals())
