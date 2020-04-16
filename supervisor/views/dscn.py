from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
def daily(request):
    dscndaily=[entry for entry in models.Dscndaily.objects.all().values()]
    return render(request,'supervisor/list_details.html',{'context':dscndaily,'name':'Dscndaily'})     

def monthly(request):
    Dscnmonthly=[entry for entry in models.Dscnmonthly.objects.all().values()]
    return render(request,'supervisor/list_details.html',{'context':Dscnmonthly,'name':'Dscnmonthly'})

def weekly(request):
    datisdaily=[entry for entry in models.Datisdaily.objects.all().values()]
    for i in datisdaily:
       if i['s_verify']==None:
           i['flag']=0
       else:
           i['flag']=1
    
    return render(request,'supervisor/daily_details.html',{'context':datisdaily,'name':'Datisdaily'})