from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
def daily(request):
    Ndbdaily=[entry for entry in models.Ndbdaily.objects.all().values()]
    return render(request,'supervisor/list_details.html',{'context':Ndbdaily,'name':'Ndbdaily'})     

def monthly(request):
    Ndbmonthly=[entry for entry in models.Ndbmonthly.objects.all().values()]
    return render(request,'supervisor/list_details.html',{'context':Ndbmonthly,'name':'Ndbmonthly'})
def weekly(request):
    return 0