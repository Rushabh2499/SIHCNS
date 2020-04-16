from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
def daily(request):
    datisdaily=[entry for entry in models.Datisdaily.objects.all().values()]
    for i in datisdaily:
       if i['s_verify']==None:
           i['flag']=0
       else:
           i['flag']=1
    
    return render(request,'supervisor/list_details.html',{'context':datisdaily,'name':'Datisdaily'})


# def monthly(request):
#     Datismonthly=[entry for entry in models.Datismonthly.objects.all().values()]
#     return render(request,'supervisor/monthly_details.html',{'context':Datismonthly,'name':'Datismonthly'}) 
def weekly(request):
    datisweekly=[entry for entry in models.Datisweekly.objects.all().values()]
    for i in datisweekly:
       if i['s_verify']==None:
           i['flag']=0
       else:
           i['flag']=1
    
    return render(request,'supervisor/list_details.html',{'context':datisweekly,'name':'Datisweekly'})