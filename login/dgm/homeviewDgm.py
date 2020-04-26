from django.shortcuts import render

from datetime import date,datetime,timedelta
from django.db import connection
from cryptography.fernet import Fernet as frt
from supervisor.views import main
from operator import itemgetter


# Create your views here.

from django.http import HttpResponse
from .. import models
from django.db import connection

def pie_chart(request):
    labels = []
    data = []

    queryset = models.DgmReports.objects.order_by('-r_count')
    for datisd in queryset:
        labels.append(datisd.r_status)
        data.append(datisd.r_count)

    return render(request, 'dgm/dgm.html', {
        'labels': labels,
        'data': data,
    })



def dgmhome(request,id):
	today = datetime.now().strftime('%d/%m/%Y')
    #request.session['type']='d'
    #request.session['uid']=uid
	return render(request,'./dgm/dgm.html')