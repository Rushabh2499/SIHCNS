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
def dhomeview(request,id) :
    request.session['uid']= id
    cursor = connection.cursor() 
    s0 = models.Engineer.objects.all()
    s0 = s0.values('a_id')
    s0 = s0.filter(emp_id=id)

    _q = models.Airport.objects
    _q = _q.filter(a_id__in=s0)
    name1 = _q.all()
                
    q = models.Engineer.objects
    q = q.values('name','designation','a_id')
    q = q.filter(emp_id=id)
    empdetails = q.all()
    ddr =0           
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='C')
    statusd = "" 
        #!!!!!!!!!!!!!!!!!datis daily!!!!!!!!!!!!!!!!!!!!!!!!
    uia = None
    currdate = date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    datisdsub_on = cursor.execute("select date from datisdaily where date = %s",[date.today()])    
    if datisdsub_on :
        statusd = models.Datisdaily.objects.all()
        statusd = statusd.values('date','status')
        statusd = statusd.order_by('-date')
        statusd = statusd.values('status')
        statusd = statusd.values('status').filter(a_id=1)[0]['status']
        if statusd == "PENDING" :
            datisdsub_on = currdate
            datisd_deadline = currdate
            ddr=0
        elif statusd == "COMPLETED" :
            datisd_deadline = currdate + timedelta(days=1)
            datisdsub_on = currdate
            ddr = 1 
        elif statusd == "COMPLETED WITH ERRORS" :
            datisd_deadline = currdate + timedelta(days=1)
            datisdsub_on = currdate
            ddr = 1
    else :
        datisd_deadline = models.Datisdaily.objects.all()
        datisd_deadline = datisd_deadline.values('date')
        datisd_deadline = datisd_deadline.order_by('-date')
        datisd_deadline = datisd_deadline.values('date').filter(a_id=1)[0]['date']
        datisdsub_on = datisd_deadline
        datisd_deadline = datisd_deadline + timedelta(days=2)
        tempdate = datisdsub_on + timedelta(days=1)
        i = 1 
        while i == 1 and tempdate != date.today() : 
         if (datisd_deadline <= date.today()) :    
            remarks = "---Report not submitted---"
            statusd = "PENDING"
            val = (tempdate,currtime,'1',id,statusd,'2',remarks)
            sql = "INSERT INTO datisdaily (date,time,a_id,emp_id,status,f_id,remarks) values (%s ,%s,%s,%s,%s, %s,%s)"
            cursor.execute(sql,val)  
            datisdsub_on = date.today()-timedelta(days=1)    
            tempdate = tempdate + timedelta(days=1)
         else : 
            break
        datisd_deadline = date.today()
          
    #!!!!!!!!!!!!!!!!!!!!!!!datis weekly!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    p_id = models.Datisweekly.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    currdate = date.today()
    wdate = models.Datisweekly.objects.all()
    wdate = wdate.values('date')
    wdate = wdate.order_by('-date')
    wdate1 = wdate
    wdate = wdate.values('date').filter(a_id=1)[0]['date']
    wdate1 = wdate1.values('date').filter(a_id=1)[1]['date']
    wdate = str(wdate)
    wdate = datetime.strptime(wdate, "%Y-%m-%d").date()
    temp = wdate
    temp1 = wdate1 + timedelta(days=7)
    wdate = wdate + timedelta(days=7) 
    dwr = 0
    datiswsub_on = temp
    datiswsub_deadline =  wdate 
    status = ""
    status = models.Datisweekly.objects.all()
    status = status.values('date','status','unit_incharge_approval')
    status = status.order_by('-date')
    uia = status
    uia = uia.values('unit_incharge_approval')
    uia = uia.values('unit_incharge_approval').filter(a_id=1)[0]['unit_incharge_approval']
    status = status.values('status')
    status = status.values('status').filter(a_id=1)[0]['status']
    flag = cursor.execute("select date from datisweekly where date = %s",[date.today()])    
    if currdate > wdate and flag == 0 :  #if it goes beyond 7 days
        pending = wdate 
        while pending <= (currdate - timedelta(days=1)) :
            f = cursor.execute("select date from datiswlogs where date = %s",[pending])    
            if f == 0 : 
                remarks = "Report not submitted"
                value = "No Entry" 
                val = (id,p_id,remarks,value,pending,currtime)
                sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s ,%s, %s,%s)"
                cursor.execute(sql,val)
            pending = pending + timedelta(days=1)    
        dwr = 0
         
    if flag :    
        if  temp1 < temp : #report submitted after deadline
            datiswsub_deadline = temp1    
            if status == "COMPLETED" or status == "COMPLETED WITH ERRORS" :
                dwr=1  
            elif status == "PENDING" :
                dwr=0
            
        elif temp == temp1 and temp == currdate : # report submitted on a day same as deadline
            datiswsub_deadline = temp    
            if status == "COMPLETED" or status == "COMPLETED WITH ERRORS" :
                dwr=1  
            elif status == "PENDING" :
                dwr=0
            
        elif temp1 < wdate and temp1 > temp : #report submitted before the deadline 
            datiswsub_deadline = temp1   
            if status == "COMPLETED" or status == "COMPLETED WITH ERRORS" :
                dwr=1  
            elif status == "PENDING" :
                dwr=0
    datisdaily=[entry for entry in models.Datisdaily.objects.filter(emp_id=id).values().order_by('-date')]
    for item in datisdaily:
        item.update( {"type":"Datisdaily"})
                
    datisweekly=[entry for entry in models.Datisweekly.objects.filter(emp_id=id).values().order_by('-date')]
    for item in datisweekly:
        item.update( {"type":"Datisweekly"})
    com=datisdaily+[i for i in datisweekly]
    com=sorted(com,key=itemgetter('date'),reverse=True)
    for i in com:
        i.update({'token':i['p_id']})
                     
                   
    '''
    #!!!!!!!!!!!!!!!!!!!!!vhfdaily!!!!!!!!!!!!!!!!!!!!!!!!
    vdr = 0
    statusvd = ""
    currdate = date.today()            
    vhfdsub_on = cursor.execute("select date from vhfdaily where date = %s",[date.today()])    
    if vhfdsub_on :
        statusvd = models.Vhfdaily.objects.all()
        statusvd = statusvd.values('date','status')
        statusvd = statusvd.order_by('-date')
        statusvd = statusvd.values('status')
        statusvd = statusvd.values('status').filter(a_id=1)[0]['status']
        if statusvd == "PENDING" :
            vhfdsub_on = currdate
            vhfd_deadline = currdate
            vdr=0
        elif statusvd == "COMPLETED" :
            vhfd_deadline = currdate + timedelta(days=1)
            vhfdsub_on = currdate
            vdr = 1 
        elif statusvd == "COMPLETED WITH ERRORS" :
            vhfd_deadline = currdate + timedelta(days=1)
            vhfdsub_on = currdate
            vdr = 1
    else :
        vhfd_deadline = models.Vhfdaily.objects.all()
        vhfd_deadline = vhfd_deadline.values('date')
        vhfd_deadline = vhfd_deadline.order_by('-date')
        vhfd_deadline = vhfd_deadline.values('date').filter(a_id=1)[0]['date']
        vhfdsub_on = vhfd_deadline
        vhfd_deadline = vhfd_deadline + timedelta(days=2)
        if (vhfd_deadline <= date.today()) :    
            remarks = "---Report not submitted---"
            statusvd = "COMPLETED"
            val = ((date.today()-timedelta(days=1)),currtime,id,'1',status,'1',remarks)
            sql = "INSERT INTO vhfdaily (date,time,emp_id,a_id,status,f_id,remarks) values (%s,%s,%s ,%s,%s, %s,%s)"
            cursor.execute(sql,val)  
            vhfdsub_on = date.today()-timedelta(days=1)    
        else : 
            vhfd_deadline = date.today()
    
    
    #!!!!!!!!!!!!!!!!!!!!!!!vhfmonthly!!!!!!!!!!!!!!!!!!!!!!!!!!!!        
    vmr = 0
    currdate = date.today()
    wdate = models.Vhfmonthly.objects.all()
    wdate = wdate.values('date')
    wdate = wdate.order_by('-date')
    wdate = wdate.values('date').filter(a_id=1)[0]['date']
    wdate = str(wdate)
    wdate = datetime.strptime(wdate, "%Y-%m-%d").date()
    temp = wdate
    wdate = wdate + timedelta(days=30) 
    #vhfmsub_on = cursor.execute("select date from vhfmonthly where date = %s",[temp])    
    vhfmsub_on = temp
    if currdate > wdate :
        vhfmsub_deadline =  currdate 
    else :
        vhfmsub_deadline =  wdate
        vmr = 1
    #!!!!!!!!!!!!!!!!!!!!!!!!vhfyearly!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    vyr = 0
    currdate = date.today()
    wdate = models.Vhfyearly.objects.all()
    wdate = wdate.values('date')
    wdate = wdate.order_by('-date')
    wdate = wdate.values('date').filter(a_id=1)[0]['date']
    wdate = str(wdate)
    wdate = datetime.strptime(wdate, "%Y-%m-%d").date()
    temp = wdate
    wdate = wdate + timedelta(days=365) 
    #vhfysub_on = cursor.execute("select date from vhfyearly where date = %s",[temp])    
    vhfysub_on = temp
    if currdate > wdate :
        vhfysub_deadline =  currdate 
    else :
        vhfysub_deadline =  wdate
        vyr = 1

    #!!!!!!!!!!!!!!!!!!!!!!!!!!dscndaily!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
    dsdr = 0
    currdate = date.today()            
    dscndsub_on = cursor.execute("select date from dscndaily where date = %s",[date.today()])    
    if dscndsub_on :
        dscnd_deadline = currdate + timedelta(days=1)
        dscndsub_on = currdate
        dsdr =1 
        
    else :
        dscnd_deadline = models.Dscndaily.objects.all()
        dscnd_deadline = dscnd_deadline.values('date')
        dscnd_deadline = dscnd_deadline.order_by('-date')
        dscnd_deadline = dscnd_deadline.values('date').filter(a_id=1)[0]['date']
        dscndsub_on = dscnd_deadline
        dscnd_deadline = dscnd_deadline + timedelta(days=2)
        if (dscnd_deadline <= date.today()) :    
            remarks = "---Report not submitted---"
            val = ((date.today()-timedelta(days=1)),id,'2',remarks)
            sql = "INSERT INTO dscndaily (date,emp_id,f_id,remarks) values (%s ,%s, %s,%s)"
            cursor.execute(sql,val)  
            dscndsub_on = date.today()-timedelta(days=1)    
        else : 
            dscnd_deadline = date.today()
   
    #!!!!!!!!!!!!!!!!!!!!!!!!dscnweekly!!!!!!!!!!!!!!!!!!!!!!!!!!
    currdate = date.today()
    wdate = models.Dscnweekly.objects.all()
    wdate = wdate.values('date')
    wdate = wdate.order_by('-date')
    wdate = wdate.values('date').filter(a_id=1)[0]['date']
    wdate = str(wdate)
    wdate = datetime.strptime(wdate, "%Y-%m-%d").date()
    temp = wdate
    wdate = wdate + timedelta(days=7) 
    dswr = 0
    dscnwsub_on = temp
    if currdate > wdate :
        dscnwsub_deadline =  currdate 
    else :
        dscnwsub_deadline =  wdate
        dswr =1 
    
    #!!!!!!!!!!!!!!!!!!!!!!!!dscnmonthly!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    dsmr = 0
    currdate = date.today()
    wdate = models.Dscnmonthly.objects.all()
    wdate = wdate.values('date')
    wdate = wdate.order_by('-date')
    wdate = wdate.values('date').filter(a_id=1)[0]['date']
    wdate = str(wdate)
    wdate = datetime.strptime(wdate, "%Y-%m-%d").date()
    temp = wdate
    wdate = wdate + timedelta(days=30) 
    dscnmsub_on = temp
    if currdate > wdate :
        dscnmsub_deadline =  currdate 
    else :
        dscnmsub_deadline =  wdate
        dsmr = 1'''
    #return render(request,'./engineer/home.html',{'status':status,'dscnmsub_deadline':dscnmsub_deadline,'dscnmsub_on':dscnmsub_on,'dsmr':dsmr,'dswr':dswr,'dscnwsub_on':dscnwsub_on,'dscnwsub_deadline':dscnwsub_deadline,'dscnd_deadline':dscnd_deadline,'dscndsub_on':dscndsub_on,'dsdr':dsdr,'ddr':ddr,'dwr':dwr,'vdr':vdr,'vmr':vmr,'vyr':vyr,'currdate':currdate,'name':name1,'id':id,'empdet':empdetails,'datisdsub_on':datisdsub_on,'datisd_deadline':datisd_deadline,'datiswsub_on':datiswsub_on,'datiswsub_deadline':datiswsub_deadline,'vhfdsub_on':vhfdsub_on,'vhfd_deadline':vhfd_deadline,'vhfmsub_on':vhfmsub_on,'vhfmsub_deadline':vhfmsub_deadline,'vhfysub_on':vhfysub_on,'vhfysub_deadline':vhfysub_deadline})
    return render(request,'./engineer/home.html',{'com':com,'wdate':wdate,'supdetails':supdetails,'statusd':statusd,'status':status,'ddr':ddr,'dwr':dwr,'currdate':currdate,'name':name1,'id':id,'empdet':empdetails,'datisdsub_on':datisdsub_on,'datisd_deadline':datisd_deadline,'datiswsub_on':datiswsub_on,'datiswsub_deadline':datiswsub_deadline})
 