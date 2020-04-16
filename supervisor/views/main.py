from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def choice(request):
    # uid=request.POST.get('daily')
    # passw=request.POST.get('monthly')
    
    if 'daily' in request.POST:
       
        # context={
        # 'cdvordaily':[entry for entry in models.Cdvordaily.objects.all().values()],
        # 'datisdaily':[entry1 for entry1 in models.Datisdaily.objects.all().values()],
        # 'dmedaily':[entry for entry in models.Dmedaily.objects.all().values()],
        # 'dscndaily':[entry for entry in models.Dscndaily.objects.all().values()],
        # 'ndbdaily':[entry for entry in models.Ndbdaily.objects.all().values()],
        # 'scctvdaily':[entry for entry in models.Scctvdaily.objects.all().values()],
        # 'vhfdaily':[entry for entry in models.Vhfdaily.objects.all().values()]
        # }
        return render(request,'supervisor/daily.html')
    if 'monthly' in request.POST:
        # context={
        # 'cdvormonthly':[entry for entry in models.Cdvormonthly.objects.all().values()],
        # # 'datisdaily':[entry1 for entry1 in models.Datisdaily.objects.all().values()],
        # 'dmemonthly':[entry for entry in models.Dmemonthly.objects.all().values()],
        # 'dscnmonthly':[entry for entry in models.Dscnmonthly.objects.all().values()],
        # 'ndbmonthly':[entry for entry in models.Ndbmonthly.objects.all().values()],
        # 'scctvmonthly':[entry for entry in models.Scctvmonthly.objects.all().values()],
        # 'vhfmonthly':[entry for entry in models.Vhfmonthly.objects.all().values()]
        # }
        return render(request,'supervisor/monthly.html')
    if 'yearly' in request.POST:
        return render(request,'supervisor/yearly.html')
    
    
    if 'weekly' in request.POST:
        context={
        'cdvorweekly':[entry for entry in models.Cdvorweekly.objects.all().values()],
        'datisweekly':[entry for entry in models.Datisweekly.objects.all().values()],
        'dmeweekly':[entry for entry in models.Dmeweekly.objects.all().values()],
        'dscnweekly':[entry for entry in models.Dscnweekly.objects.all().values()],
        'ndbweekly':[entry for entry in models.Ndbweekly.objects.all().values()],
        'scctvweekly':[entry for entry in models.Scctvweekly.objects.all().values()],
        # 'vhfmonthly':[entry for entry in models.Vhfmonthly.objects.all().values()]
        }
        context['cdvorweekly']=checkpara(context['cdvorweekly'])
        
        # defect={'defect':defect} 
        # context.update(defect)
          
        # print(defect)
        # print(context['cdvorweekly'])     
        return render(request,'supervisor/weekly.html',context)
    
    return render(request,'supervisor/supervisor.html')

def  checkpara(temp):
    err_list=[]

    count=0
    for index,i in enumerate(temp):
       if i['ps_5v']<=4:
            i['err']=1
            i['ername']='ps_5v'
       else:
            i['err']=0
       
    # print(temp)
    return temp
def details(request,id,name):
    
    if request.session['type']=='s':
            
        # print(name)
        
        str1='temp=models.'
        str2='.objects.filter(p_id='
        str3=').values()'
        que=str1+name+str2+str(id)+str3
        exec(que,globals())
        #  UNCOMMENT WHEN DONE WITH ALL LOG TABLES
        logname=name+'logs'
        logname=logname.replace('daily','d')
        logname=logname.replace('monthly','m')
        logname=logname.replace('weekly','w')
        logname=logname.replace('yearly','y')
        print(logname)
        name=name[0].lower()+name[1:]
        # logname=name+'logs'
        str1='logs=models.'
        str2='.objects.filter(p_id='
        str3=').values()'
        request.session['pid']=id
        request.session['name']=name
        que=str1+logname+str2+str(id)+str3
        exec(que,globals())
        print("logs:")
        print(logs)
        
        return render(request,'supervisor/imp_details.html',{'temp':temp[0],'names':name,'logs':logs})
        # return render(request,'supervisor/imp_details.html',{'temp':temp[0],'names':name})

def mail(request,id):
    # print(reverse("supervisor:choice"))
    # print(sid)
    mail= models.Engineer.objects.filter(emp_id=id).values('email')
    
    print(mail[0]['email'])
    return render(request,"supervisor/sendmail.html",{'eid':mail[0]['email'],'uid':id})

def sent(request):
    send=request.POST['feedback']
    
    mail_from=models.Supervisor.objects.filter(supervisor_id=request.session.get('uid')).values('email')
    print(mail_from)
    mail="From:"+mail_from[0]['email']+"\n"+send 
    str1='temp=models.'
    str2='.objects.get(p_id='
    str3=')'
    names1=request.session['name'].capitalize()
    que=str1+names1+str2+str(request.session['pid'])+str3  
    exec(que,globals())
    temp.status='PENDING'
    print("temp")
    
    temp.save()   
    print(temp)
    send_mail('urgent',mail,'aai.urgent@gmail.com',['naik.varun99@gmail.com'],fail_silently=False)
    return HttpResponse(send)

def verify(request,names,id):
    str1='temp=models.'
    str2='.objects.get(p_id='
    str3=')'
    names1=names.capitalize()
    # print('here')
    # print(names1)
    que=str1+names1+str2+str(id)+str3
    exec(que,globals())
    temp.s_verify=request.session.get('uid')
    temp.save()
    str1='context=[entry for entry in models.'
    str2='.objects.all().values()]'
   
    names1=names.capitalize()
    # print('here')
    # print(names1)
    que=str1+names1+str2
    exec(que,globals())
    for i in context:
       if i['s_verify']==None:
           i['flag']=0
       else:
           i['flag']=1
    # cdvordaily=[entry for entry in models.Cdvordaily.objects.all().values()]
    return render(request,'supervisor/list_details.html',{'context':context,'name':names1})

def empdetails(request,id):
     datisdaily=[entry for entry in models.Datisdaily.objects.filter(emp_id=id).values()]
                
     datisweekly=[entry for entry in models.Datisweekly.objects.filter(emp_id=id).values()]
     datis=datisdaily+[i for i in datisweekly]
     for i in datis:
        eng=models.Engineer.objects.filter(emp_id=i['emp_id']).values() 
        print(eng[0]['name'])
        i.update({'type':'Datisdaily','e_name':eng[0]['name'],'e_desig':eng[0]['designation']})
     return render(request,'supervisor/employee_details.html',{'datis':datis})