from django.core.mail import send_mail
from django.shortcuts import render
from .models import *

from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,"index.html",{},RequestContext(request))


def register(request):
    return render(request,"registration.html",{},RequestContext(request))



