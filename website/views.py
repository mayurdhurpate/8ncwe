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



def regsubmit(request):
    if request.method=='POST':
        u=RegUser.objects.create(Name=request.POST['Name'],
                                    Designation=request.POST['Designation'],
                                    Organisation=request.POST['Organisation'],
                                    Address= request.POST['Address']   ,
                                    Mob=request.POST['Mob'],
                                    Email=request.POST['Email'] ,
                                    Membership=request.POST['Membership'],
                                    DD=request.POST['DD'] ,
                                    Amount=request.POST['Amount'] ,
                                    Bank=request.POST['Bank'] ,
                                    Branch=request.POST['Branch'] ,
                                    Date=request.POST['Date'])


      

        
        # send_mail(
        #     'Subject here',
        #     'Thanks for submission. We have recorded your response.\nTitle of Paper'+u.Name+'\nName of 1st Author'+u.Mob+'\nCollege/university'
        #     +u.college+'\ndesignation'+u.designation+'\nCo-Author'+u.coauthor+'\nPhone No.'+u.phone+'\nEmail'+u.email,
        #     'no-reply@shilpiitbhu.org',
        #     [u.email],
        #     fail_silently=False,
        # )
        return HttpResponse('Your response have been recorded.')
    return HttpResponse('Authentication failed.')