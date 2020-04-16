from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
def daily(request):
    Vhfdaily=[entry for entry in models.Vhfdaily.objects.all().values()]
    return render(request,'supervisor/list_details.html',{'context':Vhfdaily,'name':'Vhfdaily'})  
def monthly(request):
    Vhfmonthly=[entry for entry in models.Vhfmonthly.objects.all().values()]
    return render(request,'supervisor/list_details.html',{'context':Vhfmonthly,'name':'Vhfmonthly'})  
def weekly(request):
    return 0 