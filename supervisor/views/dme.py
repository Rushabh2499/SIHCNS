from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
def daily(request):
    dmedaily=[entry for entry in models.Dmedaily.objects.all().values()]
    return render(request,'supervisor/list_details.html',{'context':dmedaily,'name':'Dmedaily'})

def monthly(request):
    Dmemonthly=[entry for entry in models.Dmemonthly.objects.all().values()]
    return render(request,'supervisor/list_details.html',{'context':Dmemonthly,'name':'Dmemonthly'})     
def weekly(request):
    return 0