from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from login.models import Engineer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from datetime import date,datetime,timedelta
from django.db import connection
from cryptography.fernet import Fernet as frt
from supervisor.views import main
from login.sup.homeviewSup import run_sup as run_sup
from login.eng.homeviewEng import dhomeview as dhomeview
from login.dgm.homeviewDgm import pie_chart as pie_chart
from login.eng.logEng import logEng as logEng
from head.views import dispMap as dispMap

# Create your views here.

from django.http import HttpResponse
from . import models
from django.db import connection
# Create your views here.
def login(request):
    # key=frt.generate_key()
    # f=frt(key)
    # request.session['key']=f
    # print("key")
    # print(request.session['key'])
    if request.session.has_key('uid') and request.session.get('type')=='e':
         return logEng(request,request.session.get('uid'))
         
    if request.session.has_key('uid') and request.session.get('type')=='s':
        return run_sup(request,request.session.get('uid'))

    if request.session.has_key('uid') and request.session.get('type')=='d':
        return logDgm(request,request.session.get('uid'))
    else:
         return render(request,'login/login.html')

def validate(request):
    
    uid=request.POST.get('id',False)
    passw=request.POST.get('passw',False)
    print(uid)
    print(passw)
    #if (uid==False and passw==False):
     #  uid=request.session['uid']
      #  passw=request.session['passw']
    #if (uid=='' and passw==''):
     #   return render(request,'login/login.html')
    flag=1

        # for

            # print(type(uid))
            # print(i.password)
            # print(i.designation)
    temp=uid
    id = uid
    b=temp[0]+""+temp[1]
    if b=='41' :
        x=models.Engineer.objects.all()
        for i in x:  
            if (uid == str(i.emp_id)) & (check_password(passw,i.password)) :
                flag=0
                request.session['type']='e'
                return dhomeview(request,id) 
    elif b=='21' :
        x=models.Dgm.objects.all()
        for i in x:
            if (uid == str(i.dgm_id)) & (check_password(passw,i.password)) :
                flag=0
                request.session['type']='d'
                return pie_chart(request)
    elif b=='11' :
        x=models.Head.objects.all()
        for i in x:
            if (uid == str(i.head_id)) & (check_password(passw,i.password)) :

                    flag=0

                    # y=models.Airport.objects.filter(a_id=i.a_id).values()
                    # print(y[0])
                    airInfo=models.Airport.objects.all().values()
                    # request.session['dept']=supInfo[0]['dept']
                    return dispMap(request,airInfo)
    elif b=='31' :
        # key=frt.generate_key()
        # f=frt(key)
        request.session['key']=frt.generate_key().decode('utf-8')
        # print("key")
        # print(request.session['key'])
                   
        x=models.Supervisor.objects.all()
        for i in x:
            print(check_password(passw,i.password))
            if (uid == str(i.supervisor_id)) & (check_password(passw,i.password)) :

                flag=0

                # y=models.Airport.objects.filter(a_id=i.a_id).values()
                # print(y[0])
                supInfo=models.Supervisor.objects.filter(supervisor_id=uid).values()
                request.session['dept']=supInfo[0]['dept']
                return run_sup(request,uid)
                



            #
            # if(i.designation=='DGM'):
            #     y=models.Airport.objects.filter(a_id=i.a_id).values()
            #     print(y[0])
            #     return render(request,'seek/dgm.html',y[0])
            # elif (i.designation=='ED-CNS'):
            #     print("here")
            #     return render(request,'seek/head.html')
            # else:
            #         return render(request,'seek/engineer.html')
            #         break



    if flag==1 :
            print("wrong")
            return render(request,'login/login.html',{'flag':flag})

            



def std(request,id) :
     if request.session.has_key('uid'):
        return render(request,'login/standards.html')  
     else :
        return render(request,'login/login.html')     

