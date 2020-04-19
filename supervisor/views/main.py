from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
from django.db import connection
import datetime
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from cryptography.fernet import Fernet as frt

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
        # context={
        # 'cdvorweekly':[entry for entry in models.Cdvorweekly.objects.all().values()],
        # 'datisweekly':[entry for entry in models.Datisweekly.objects.all().values()],
        # 'dmeweekly':[entry for entry in models.Dmeweekly.objects.all().values()],
        # 'dscnweekly':[entry for entry in models.Dscnweekly.objects.all().values()],
        # 'ndbweekly':[entry for entry in models.Ndbweekly.objects.all().values()],
        # 'scctvweekly':[entry for entry in models.Scctvweekly.objects.all().values()],
        # # 'vhfmonthly':[entry for entry in models.Vhfmonthly.objects.all().values()]
        # }
        # context['cdvorweekly']=checkpara(context['cdvorweekly'])
        
        # defect={'defect':defect} 
        # context.update(defect)
          
        # print(defect)
        # print(context['cdvorweekly'])     
        return render(request,'supervisor/weekly.html',context)
    
    return render(request,'supervisor/home.html')

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
    id=decode(request,id)
    if request.session.get('type')=='s':
            
        # print(name)
        
        str1='temp=models.'
        str2='.objects.filter(p_id='
        str3=').values()'
        str4='.objects.all('
        que=str1+name+str2+str(id)+str3
        exec(que,globals())
        str1='mrec=models.'
        que=str1+name+str4+str3+".order_by('-date')"
        exec(que,globals())
        #  UNCOMMENT WHEN DONE WITH ALL LOG TABLES
        logname=name+'logs'
        logname=logname.replace('daily','d')
        logname=logname.replace('monthly','m')
        logname=logname.replace('weekly','w')
        logname=logname.replace('yearly','y')
        print(logname)
        name=name[0].lower()+name[1:]
        # # logname=name+'logs'
        str1='logs=models.'
        str2='.objects.filter(p_id='
        str3=').values()'
        request.session['pid']=id
        request.session['name']=name
        que=str1+logname+str2+str(id)+str3
        exec(que,globals())
        # print("logs:")
        # print(logs)
        i=temp[0]
        i['e_token']=encode(request,str(i['emp_id']))
        i['p_token']=encode(request,str(i['p_id']))
        eng=models.Engineer.objects.filter(emp_id=temp[0]['emp_id']).values()
        # print(i)
        redir='supervisor:'+name
        return render(request,'supervisor/imp_details.html',{'eng':eng[0],'temp':i,'names':name,'redir':redir,'logs':logs,'mrec':mrec})
        # return render(request,'supervisor/imp_details.html',{'temp':i,'names':name})

def mail(request,id):
    # print(reverse("supervisor:choice"))
    # print(sid)
    id=decode(request,id)
    mail= models.Engineer.objects.filter(emp_id=id).values('email')
    
    print(mail[0]['email'])
    
    return render(request,"supervisor/sendmail.html",{'eid':mail[0]['email'],'uid':id})

def sent(request):
    send=request.POST['feedback']
    print(send)
    mail_from=models.Supervisor.objects.filter(supervisor_id=request.session.get('uid')).values('email')
    print(mail_from)
    mail="From:"+mail_from[0]['email']+"\n"+send 
    str1='temp=models.'
    str2='.objects.get(p_id='
    str3=')'
    names1=request.session['name'].capitalize()
    pid=request.session['pid']
    que=str1+names1+str2+str(request.session['pid'])+str3
    del request.session['name']
    del request.session['pid']
    exec(que,globals())
    now = datetime.datetime.now()
    date=now.strftime("%Y-%m-%d")
    time=now.strftime("%H:%M:%S")
    temp.approval_date=date
    temp.approval_time=time
    temp.unit_incharge_approval='NO'
    print("temp")
    temp.status="PENDING"
    temp.save()
      
    print(temp)
    send_mail('urgent',mail,'aai.urgent@gmail.com',['naik.varun99@gmail.com'],fail_silently=False)
    # return render(request,'supervisor/imp_details.html',{'temp':temp[0],'names':names1,'logs':logs})
    return HttpResponseRedirect(reverse('supervisor:details',kwargs={'id':encode(request,str(pid)), 'name':names1}))

def verify(request,names,id):
    ids=id
    id=decode(request,id)
    print(id)
    str1='temp=models.'
    str2='.objects.get(p_id='
    str3=')'
    names1=names.capitalize()
  
    que=str1+names1+str2+id+str3
    print(que)
    exec(que,globals())
    now = datetime.datetime.now()
    date=now.strftime("%Y-%m-%d")
    time=now.strftime("%H:%M:%S")
    temp.unit_incharge_approval='YES'
    temp.approval_date=date
    temp.approval_time=time
    temp.save()
    str1='context=[entry for entry in models.'
    str2='.objects.all().values()]'
    now = datetime.datetime.now()
    names1=names.capitalize()
    # print('here')
    # print(names1)
    que=str1+names1+str2
    
    exec(que,globals())
    for i in context:
       i['token']=encode(request,str(i['p_id'])) 
       if i['unit_incharge_approval']=='YES':
           i['flag']=1
       elif i['unit_incharge_approval']=='NO':
           i['flag']=0
       else:
            i['flag']='not set'
    # cdvordaily=[entry for entry in models.Cdvordaily.objects.all().values()]
    print("com")
    print(context)
   
    return HttpResponseRedirect(reverse('supervisor:details',kwargs={'id':ids, 'name':names1}))

def empdetails(request,id):
     id=decode(request,id)
     datisdaily=[entry for entry in models.Datisdaily.objects.filter(emp_id=id).values().order_by('-date')]
     eng=models.Engineer.objects.filter(emp_id=id).values()          
     datisweekly=[entry for entry in models.Datisweekly.objects.filter(emp_id=id).values().order_by('-date')]
     datis=datisdaily+[i for i in datisweekly]
     print(datis)
     for i in datis:
        # eng=models.Engineer.objects.filter(emp_id=i['emp_id']).values()
         
        
        i.update({'type':'Datisdaily','token':encode(request,str(i['p_id']))})
        # print(i['e_name'])
    #  print(datis)
     return render(request,'supervisor/employee_details.html',{'datis':datis,'e_name':eng[0]['name'],'e_desig':eng[0]['designation'],'e_contact':eng[0]['contact'],'e_email':eng[0]['email']})

def encode(request,s):

    f=frt(request.session['key'].encode('utf-8'))
    token = f.encrypt(s.encode('utf-8'))
    # print(token.decode('utf-8'))
    return token.decode('utf-8')

def decode(request,s):
    f=frt(request.session['key'].encode('utf-8'))
    token = f.decrypt(s.encode('utf-8'))
    # print(token.decode('utf-8'))
    return token.decode('utf-8')

