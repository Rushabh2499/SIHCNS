from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
def daily(request):
    Scctvdaily=[entry for entry in models.Scctvdaily.objects.all().values()]
    return render(request,'supervisor/list_details.html',{'context':Scctvdaily,'name':'Scctvdaily'})     

def monthly(request):
    Scctvmonthly=[entry for entry in models.Scctvmonthly.objects.all().values()]
    return render(request,'supervisor/list_details.html',{'context':Scctvmonthly,'name':'Scctvmonthly'})

def weekly(request):
    return 0