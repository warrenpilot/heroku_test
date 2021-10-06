from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required

#Python Packages
import os

@login_required
def home_page(request):
    template = loader.get_template('home/index.html')
    context = {    
    }
    return HttpResponse(template.render(context, request))
    
