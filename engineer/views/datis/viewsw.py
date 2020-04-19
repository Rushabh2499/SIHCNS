from django.shortcuts import render
from django.db import connection
from datetime import date,datetime,timedelta
# Create your views here.
from login import models as models

def datisweeklyrec(request, id):
  if request.session.has_key('uid'):
    cursor = connection.cursor() 
    datis_w = models.Datisweekly.objects.all()
    datis_w = datis_w.values('p_id','date','time','status','serveraorb','ups_ip','ups_op','dust_free','lan_status','unit_incharge_approval','approval_date','approval_time')
    datis_w = datis_w.filter(emp_id=id)
    return render(request,'engineer/datis/datiswrecords.html',{'datis_w':datis_w,'id':id}) 
  else : 
    return render(request,'login/login.html')
    
def datisw(request, id) :
  if request.session.has_key('uid'):
    datis_w = models.Datisweekly.objects.all()
    datis_w = datis_w.values('p_id','date','time','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
    datis_w = datis_w.filter(emp_id=id)
    datisw = datis_w
    datis_w = datis_w.filter(date=date.today())
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='C')
    datiswlogs = models.Datiswlogs.objects.all()
    datiswlogs = datiswlogs.filter(date=date.today())    
    
    if datis_w :
       return render(request,'engineer/datis/datisweeklyrep.html',{'datiswlogs':datiswlogs,'supdetails':supdetails,'datis_w':datis_w,'id':id,'datisw':datisw}) 
    else :
       messages.add_message(request,30, 'You cannot make changes to pending report!')
       return routebackdatisd(request, id)
  
  else : 
    return render(request,'login/login.html')
   
def datiswrep(request, id) :
    datis_w = models.Datisweekly.objects.all()
    datis_w = datis_w.values('p_id','date','time','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
    datis_w = datis_w.filter(emp_id=id)
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='C')
   
    return render(request,'engineer/datis/datiswrepsub.html',{'datis_w':datis_w,'id':id,'supdetails':supdetails}) 
    
def datiswrepsubw(request, id) :  
    a_id = models.Engineer.objects.all()
    a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id'] 
    currtime = datetime.now().strftime("%H:%M:%S")
    emp_id = models.Datisweekly.objects.all()
    emp_id = emp_id.values('emp_id').filter(emp_id=id)[0]['emp_id']
    currdate= date.today()
    cursor = connection.cursor() 
    serveraorb=''
    upsip=''
    upsop=''
    dustfree=''
    lanstatus=''
    serveraorb=request.POST['serverAorB']
    upsip1 = request.POST['UPS_ip']
    upsop1 = request.POST['UPS_op']
    dustfree =request.POST['Dust_free']
    lanstatus =request.POST['LAN_status']
    upsip = int(upsip1)
    upsop = int(upsop1)
    
    sql = "INSERT INTO datisweekly (date,time,a_id,f_id,emp_id,status,serverAorB,UPS_ip,UPS_op,Dust_free,LAN_status) VALUES (%s,%s,%s,%s,%s,%s, %s,%s, %s, %s, %s)"
    val = (currdate,currtime,a_id,'2',id,"",serveraorb,upsip,upsop,dustfree,lanstatus)
    cursor.execute(sql, val)
    p_id = models.Datisweekly.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    print(p_id)
    f=2
    if serveraorb != 'A' :  
        if serveraorb != 'B' :
            f=3
            remarks = "Incorrent entry"
            val = (id,p_id,remarks,serveraorb,currdate,currtime)
            sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
            cursor.execute(sql,val)
    
    
    if upsip < 200 or upsip > 230  :
        f=3
        remarks = "UPS_ip not in corrent range"
        val = (id,p_id,remarks,upsip,currdate,currtime)
        sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
        
    if upsop != 230 :
        f=3
        remarks = "UPS_op value not normal"
        val = (id,p_id,remarks,upsop,currdate,currtime)
        sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    if dustfree != 'OK' :
        f=3
        remarks = "Not Dustfree"
        val = (id,p_id,remarks,dustfree,currdate,currtime)
        sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val) 
    if lanstatus != 'OK' :
        f=3
        remarks = "Lan status not OK"
        val = (id,p_id,remarks,lanstatus,currdate,currtime)
        sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    
    if f == 2:
        status = "COMPLETED"
        remarks = "Parameters normal at the first submit!"
        value = "All parameters NORMAL"
        val = (id,p_id,remarks,value,currdate,currtime)
        sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        status = "PENDING"    
    print(status)    
    cursor.execute("update datisweekly set status = %s where p_id = %s",[status,p_id])
    datis_w = models.Datisweekly.objects.all()
    datis_w = datis_w.values('p_id','date','time','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
    datisw = datis_w.filter(emp_id=id)
    datis_w = datis_w.filter(date=currdate)
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='C')
    datiswlogs = models.Datiswlogs.objects.all()
    datiswlogs = datiswlogs.filter(date=date.today())    
    
    return render(request,'engineer/datis/datisweeklyrep.html',{'datiswlogs':datiswlogs,'datis_w':datis_w,'id':id,'datisw':datisw,'supdetails':supdetails})      

def editdatisweekly(request, p_id) :
    cursor = connection.cursor() 
    emp_id = models.Datisweekly.objects.all()
    emp_id = emp_id.values('emp_id').filter(p_id=p_id)[0]['emp_id']
    datisw = models.Datisweekly.objects.all()
    datisw = datisw.values('p_id','date','time','emp_id','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
    datis_w = datisw.filter(emp_id=emp_id)
    datisw = datisw.filter(p_id=p_id)
    datis_id = datisw.values('p_id').filter(p_id=p_id)[0]['p_id']
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='C')
    datiswlogs = models.Datiswlogs.objects.all()
    datiswlogs = datiswlogs.filter(date=date.today())    
     
    return render(request,'engineer/datis/editdatiswrepsub.html',{'datiswlogs':datiswlogs,'datisw':datisw,'id':datis_id,'datis_w':datis_w,'supdetails':supdetails})

def updatisweekly(request, id) :
    p_id = models.Datisweekly.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    currdate= date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    emp_id = models.Datisweekly.objects.all()
    emp_id = emp_id.values('emp_id').filter(p_id=id)[0]['emp_id']
    cursor = connection.cursor() 
    serveraorb=''
    upsip=''
    upsop=''
    dustfree=''
    lanstatus=''
    remarks=request.POST['remarks']
    serveraorb=request.POST['serverAorB']
    upsip1 = request.POST['UPS_ip']
    upsop1 = request.POST['UPS_op']
    dustfree =request.POST['Dust_free']
    lanstatus =request.POST['LAN_status']
    upsip = int(upsip1)
    upsop = int(upsop1)
    
    f=2
    if serveraorb != 'A' :  
        if serveraorb != 'B' :
            f=3
            cursor.execute("update datisweekly set serverAorB = %s where p_id = %s",[serveraorb,id])
            #remarks = "Incorrent entry(update)" 
            val = (emp_id,p_id,remarks,serveraorb,currdate,currtime)
            sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
            cursor.execute(sql,val)
        else :
            cursor.execute("update datisweekly set serverAorB = %s where p_id = %s",[serveraorb,id])    
    
    if upsip < 200 or upsip > 230  :
        f=3
        cursor.execute("update datisweekly set UPS_ip = %s where p_id = %s",[upsip,id])
        #remarks = "UPS_ip not in correct range(update)"
        val = (emp_id,p_id,remarks,serveraorb,currdate,currtime)
        sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update datisweekly set UPS_ip = %s where p_id = %s",[upsip,id])
            
    if upsop != 230 :
        f=3
        cursor.execute("update datisweekly set UPS_op = %s where p_id = %s",[upsop,id])
        #remarks = "UPS_op value not normal(update)"
        val = (emp_id,p_id,remarks,serveraorb,currdate,currtime)
        sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update datisweekly set UPS_op = %s where p_id = %s",[upsop,id])
    
    if dustfree != 'OK' :
        f=3
        cursor.execute("update datisweekly set Dust_free = %s where p_id = %s",[dustfree,id])
        #remarks = "Not Dustfree(update)"
        val = (emp_id,p_id,remarks,serveraorb,currdate,currtime)
        sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val) 
    else :
        cursor.execute("update datisweekly set Dust_free = %s where p_id = %s",[dustfree,id])
    
    if lanstatus != 'OK' :
        f=3
        cursor.execute("update datisweekly set LAN_status = %s where p_id = %s",[lanstatus,id])
        #remarks = "Lan status not OK(update)"
        val = (emp_id,p_id,remarks,serveraorb,currdate,currtime)
        sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update datisweekly set LAN_status = %s where p_id = %s",[lanstatus,id])

    if ((serveraorb == 'A' or serveraorb == 'B') and (upsip > 199 and upsip < 231) and (upsop == 230) and (dustfree == 'OK') and (lanstatus == 'OK')) :
        cursor.execute("update datisweekly set serverAorB = %s where p_id = %s",[serveraorb,id]) 
        cursor.execute("update datisweekly set UPS_ip = %s where p_id = %s",[upsip,id])  
        cursor.execute("update datisweekly set UPS_op = %s where p_id = %s",[upsop,id]) 
        cursor.execute("update datisweekly set Dust_free = %s where p_id = %s",[dustfree,id])
        cursor.execute("update datisweekly set LAN_status = %s where p_id = %s",[lanstatus,id])
        cursor.execute("update datisweekly set status = %s where p_id = %s",["COMPLETED",id])
        remarks = "Parameter/s fixed"
        value = "All parameters NORMAL"
        val = (emp_id,p_id,remarks,serveraorb,currdate,currtime)
        sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    datis_w = models.Datisweekly.objects.all()
    datis_w = datis_w.values('p_id','date','time','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
    datisw = datis_w.filter(emp_id=emp_id)
    datis_w = datis_w.filter(date=currdate)
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='C')
    datiswlogs = models.Datiswlogs.objects.all()
    datiswlogs = datiswlogs.filter(date=date.today())    
    return render(request,'engineer/datis/datisweeklyrep.html',{'datiswlogs':datiswlogs,'datis_w':datis_w,'id':emp_id,'datisw':datisw,'supdetails':supdetails})      

def repsubwerrors(request,p_id,id):
    cursor = connection.cursor() 
    datisw = models.Datisweekly.objects.all()
    datisw = datisw.values('p_id','date','time','emp_id','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
    datisw = datisw.filter(p_id=p_id)
    return render(request,'engineer/datis/datiswfinalrep.html',{'datisw':datisw,'p_id':p_id,'id':id})

def finalwrepsub(request,p_id,id):
    f=1
    print(f)
    cursor = connection.cursor()
    currdate= date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    remarks = request.POST['remarks']
    print(remarks)
    value = "Final submit with errors"
    val = (id,p_id,remarks,value,currdate,currtime)
    sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
    cursor.execute(sql,val)
    cursor.execute("update datisweekly set status = %s where p_id = %s",["COMPLETED WITH ERRORS",p_id])
    cursor.execute("update datisweekly set unit_incharge_approval = %s where p_id = %s",[None,p_id])
   
    #code for notification to supervisor will come over here 
    if request.session.has_key('uid'):
        cursor = connection.cursor() 
        currdate = date.today()
        datis_w = models.Datisweekly.objects.all()
        datis_w = datis_w.values('p_id','date','time','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
        datisw = datis_w.filter(emp_id=id)
        datis_w = datis_w.filter(date=currdate)
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='C')
        datiswlogs = models.Datiswlogs.objects.all()
        datiswlogs = datiswlogs.filter(date=date.today())    
    
        return render(request,'engineer/datis/datisweeklyrep.html',{'datiswlogs':datiswlogs,'datis_w':datis_w,'id':id,'f':f,'datisw':datisw,'supdetails':supdetails})      
    else : 
        return render(request,'login/login.html')


