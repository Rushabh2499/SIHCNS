from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
def daily(request):
    cdvordaily=[entry for entry in models.Cdvordaily.objects.all().values()]
    for i in cdvordaily:
       if i['s_verify']==None:
           i['flag']=0
       else:
           i['flag']=1

    return render(request,'supervisor/list_details.html',{'context':cdvordaily,'name':'Cdvordaily'}) 

def weekly(request):
    cdvorweekly=[entry for entry in models.Cdvorweekly.objects.all().values()]
    for i in cdvordaily:
       if i['s_verify']==None:
           i['flag']=0
       else:
           i['flag']=1

    return render(request,'supervisor/list_details.html',{'context':cdvorweekly,'name':'Cdvorweekly'})         

def monthly(request):
    cdvormonthly=[entry for entry in models.Cdvormonthly.objects.all().values()]
    return render(request,'supervisor/list_details.html',{'context':cdvormonthly,'name':'Cdvormonthly'})     
    