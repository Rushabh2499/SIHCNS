from django.shortcuts import render
from django.db import connection
from datetime import date,datetime,timedelta
# Create your views here.
from login import models as models

def routebackdscnd(request,id):
  if request.session.has_key('uid'):
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
        #!!!!!!!!!!!!!!!!!datis daily!!!!!!!!!!!!!!!!!!!!!!!!
    currdate = date.today()            
    datisdsub_on = cursor.execute("select date from datisdaily where date = %s",[date.today()])    
    if datisdsub_on :
        datisd_deadline = currdate + timedelta(days=1)
        datisdsub_on = currdate
        ddr =1 
        
    else :
        datisd_deadline = models.Datisdaily.objects.all()
        datisd_deadline = datisd_deadline.values('date')
        datisd_deadline = datisd_deadline.order_by('-date')
        datisd_deadline = datisd_deadline.values('date').filter(a_id=1)[0]['date']
        datisdsub_on = datisd_deadline
        datisd_deadline = datisd_deadline + timedelta(days=2)
        if (datisd_deadline <= date.today()) :    
            remarks = "---Report not submitted---"
            val = ((date.today()-timedelta(days=1)),id,'2',remarks)
            sql = "INSERT INTO datisdaily (date,emp_id,f_id,remarks) values (%s ,%s, %s,%s)"
            cursor.execute(sql,val)  
            datisdsub_on = date.today()-timedelta(days=1)    
        else : 
            datisd_deadline = date.today()
    
    #!!!!!!!!!!!!!!!!!!!!!!!datis weekly!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  
    currdate = date.today()
    wdate = models.Datisweekly.objects.all()
    wdate = wdate.values('date')
    wdate = wdate.order_by('-date')
    wdate = wdate.values('date').filter(a_id=1)[0]['date']
    wdate = str(wdate)
    wdate = datetime.strptime(wdate, "%Y-%m-%d").date()
    temp = wdate
    wdate = wdate + timedelta(days=7) 
    #datiswsub_on = cursor.execute("select date from datisweekly where date = %s",[wdate])    
    dwr = 0
    #if datiswsub_on :
     #   datiswsub_on = temp
     #   datiswsub_deadline =  wdate 
     #   dwr = 1
    #else :
    datiswsub_on = temp
    if currdate > wdate :
        datiswsub_deadline =  currdate 
    else :
        datiswsub_deadline =  wdate
        dwr =1 
    print(dwr)
    #!!!!!!!!!!!!!!!!!!!!!vhfdaily!!!!!!!!!!!!!!!!!!!!!!!!
    vdr = 0
    currdate = date.today()            
    vhfdsub_on = cursor.execute("select date from vhfdaily where date = %s",[date.today()])    
    if vhfdsub_on :
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
            val = ((date.today()-timedelta(days=1)),id,'2',remarks)
            sql = "INSERT INTO vhfdaily (date,emp_id,f_id,remarks) values (%s ,%s, %s,%s)"
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
        dsmr = 1
    
    return render(request,'./engineer/home.html',{'dscnmsub_deadline':dscnmsub_deadline,'dscnmsub_on':dscnmsub_on,'dsmr':dsmr,'dswr':dswr,'dscnwsub_on':dscnwsub_on,'dscnwsub_deadline':dscnwsub_deadline,'dscnd_deadline':dscnd_deadline,'dscndsub_on':dscndsub_on,'dsdr':dsdr,'ddr':ddr,'dwr':dwr,'vdr':vdr,'vmr':vmr,'vyr':vyr,'currdate':currdate,'name':name1,'id':id,'empdet':empdetails,'datisdsub_on':datisdsub_on,'datisd_deadline':datisd_deadline,'datiswsub_on':datiswsub_on,'datiswsub_deadline':datiswsub_deadline,'vhfdsub_on':vhfdsub_on,'vhfd_deadline':vhfd_deadline,'vhfmsub_on':vhfmsub_on,'vhfmsub_deadline':vhfmsub_deadline,'vhfysub_on':vhfysub_on,'vhfysub_deadline':vhfysub_deadline})
  else :
    return render(request,'login/login.html')  

def dscndailylogs(request, id) :
  if request.session.has_key('uid'):
     cursor = connection.cursor() 
     dscn_d = models.Dscndaily.objects.all()
     dscn_d = dscn_d.values('dscndaily_id','date','time','sat_led','odu_led','io_led','alarm_led','power_led','v35_led','ip_voltage','op_voltage','battery_voltage','coro_function','remarks','unit_incharge_approval')
     f=1
     return render(request,'engineer/dscn/dscndailyrep.html',{'dscn_d':dscn_d,'id':id,'f':f})
  else :
     return render(request,'login/login.html')
   
    
def dscnd(request, id) :
  if request.session.has_key('uid'):
     cursor = connection.cursor() 
     dscn_d = models.Dscndaily.objects.all()
     dscn_d = dscn_d.values('dscndaily_id','date','time','sat_led','odu_led','io_led','alarm_led','power_led','v35_led','ip_voltage','op_voltage','battery_voltage','coro_function','remarks','unit_incharge_approval')
     currdate = date.today()
     cdate = cursor.execute("select date from dscndaily where date = %s",[currdate])    
     print(cdate)
     f=0
     return render(request,'engineer/dscn/dscndailyrep.html',{'dscn_d':dscn_d,'id':id,'f':f})
  else :
     return render(request,'login/login.html')
   

def dscndrep(request, id):
     return render(request,'engineer/dscn/dscnrepsub.html',{'id':id})      

def dscndrepsub(request,id):
     cursor = connection.cursor()
     currdate= date.today()
     currtime = datetime.now().strftime("%H:%M:%S")
     a_id = models.Engineer.objects.all()
     a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id']
     sled = request.POST['sled']
     oled = request.POST['oled']
     ioled=request.POST['ioled']
     aled = request.POST['aled']
     pwled = request.POST['pwled']
     v35led = request.POST['v35led']
     iv = request.POST['iv']
     ov = request.POST['ov']
     bv=request.POST['bv']
     cof = request.POST['cof']
     rmarks = request.POST['remarks']
     f=2
     if sled != 'STEADY ON' :
         f=3
         remarks = "SAT LED not steady on"
         val = (id,remarks,sled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     if oled != 'STEADY ON' :
         f=3
         remarks = "ODU LED not steady on"
         val = (id,remarks,oled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     if sled != 'STEADY ON' :
         f=3
         remarks = "I/O LED not steady on"
         val = (id,remarks,ioled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     if pwled != 'STEADY ON' :
         f=3
         remarks = "Power LED not steady on"
         val = (id,remarks,pwled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
        
     if v35led != 'RX/TX BLINKING' :
         f=3
         remarks = "Rx/Tx -not Blinking"
         val = (id,remarks,v35led,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
         
     if aled != 'OFF' :
         f=3
         remarks = "Alarm LED was turned ON"
         val = (id,remarks,aled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     
     if int(iv) < 220 or int(iv) > 240 :
         f=3
         remarks = "UPS I/P Voltage exceeding normal voltage"
         val = (id,remarks,iv,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     if int(ov) < 220 or int(ov) > 240 :
         f=3
         remarks = "UPS O/P Voltage exceeding normal voltage"
         val = (id,remarks,ov,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     if int(bv) < 180 or int(bv) > 250 :
         f=3
         remarks = "UPS Battery Voltage exceeding normal voltage"
         val = (id,remarks,bv,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
      
     if  cof != 'OK' :
         f=3
         remarks = "C/O Function not OK"
         val = (id,remarks,cof,currdate,currtime)
         sql = "INSERT INTO vhfdlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
    
     if f == 2 :
          uincharappro = "YES"
          f=1
     else :
          f=2
          uincharappro = "NO"      
 
     sql = "INSERT INTO dscndaily (date,time,a_id,emp_id,SAT_LED,ODU_LED,IO_LED,Alarm_LED,Power_LED,V35_LED,IP_Voltage,OP_voltage,Battery_Voltage,CorO_function,remarks,Unit_Incharge_Approval) VALUES (%s, %s,%s,%s,%s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)"
     val = (currdate,currtime,a_id,id,sled,oled,ioled,aled,pwled,v35led,iv,ov,bv,cof,rmarks,uincharappro)
     cursor.execute(sql, val)
     dscn_d = models.Dscndaily.objects.all()
     dscn_d = dscn_d.values('dscndaily_id','date','time','sat_led','odu_led','io_led','alarm_led','power_led','v35_led','ip_voltage','op_voltage','battery_voltage','coro_function','remarks','unit_incharge_approval')
     return render(request,'engineer/dscn/dscndailyrep.html',{'dscn_d':dscn_d,'id':id,'flag':f})

def editdscndaily(request,dscndaily_id):
     cursor = connection.cursor() 
     dscn_d = models.Dscndaily.objects.all()
     dscn_d = dscn_d.values('dscndaily_id','date','time','emp_id','sat_led','odu_led','io_led','alarm_led','power_led','v35_led','ip_voltage','op_voltage','battery_voltage','coro_function','remarks','unit_incharge_approval')
     dscnd = dscn_d.filter(dscndaily_id=dscndaily_id)
     dscnd_id = dscnd.values('dscndaily_id').filter(dscndaily_id=dscndaily_id)[0]['dscndaily_id']
     return render(request,'engineer/dscn/editdscnrepsub.html',{'dscnd':dscnd,'id':dscnd_id}) 

def updscndaily(request, id) :
     cursor = connection.cursor() 
     currtime = datetime.now().strftime("%H:%M:%S")
     emp_id = models.Vhfdaily.objects.all()
     emp_id = emp_id.values('emp_id').filter(vhfdaily_id=id)[0]['emp_id']
     currdate= date.today()
     sled = request.POST['sled']
     oled = request.POST['oled']
     ioled=request.POST['ioled']
     aled = request.POST['aled']
     pwled = request.POST['pwled']
     v35led = request.POST['v35led']
     iv = request.POST['iv']
     ov = request.POST['ov']
     bv=request.POST['bv']
     cof = request.POST['cof']
     rmarks = request.POST['remarks']
     f=2
     if sled != 'STEADY ON' :
         f=3
         cursor.execute("update dscndaily set SAT_LED = %s where dscndaily_id = %s",[sled,id])
         remarks = "SAT LED not steady on(update)"
         val = (emp_id,remarks,sled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set SAT_LED = %s where dscndaily_id = %s",[sled,id])
              
     if oled != 'STEADY ON' :
         f=3
         cursor.execute("update dscndaily set ODU_LED = %s where dscndaily_id = %s",[oled,id])
         remarks = "ODU LED not steady on(update)"
         val = (emp_id,remarks,oled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set ODU_LED = %s where dscndaily_id = %s",[oled,id])
          
     if ioled != 'STEADY ON' :
         f=3
         cursor.execute("update dscndaily set IO_LED = %s where dscndaily_id = %s",[ioled,id])
         remarks = "IO LED not steady on(update)"
         val = (emp_id,remarks,oled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set IO_LED = %s where dscndaily_id = %s",[ioled,id])
    
     if pwled != 'STEADY ON' :
         f=3
         cursor.execute("update dscndaily set Power_LED = %s where dscndaily_id = %s",[pwled,id])
         remarks = "Power LED not steady on(update)"
         val = (emp_id,remarks,pwled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set Power_LED = %s where dscndaily_id = %s",[pwled,id])
            
     if v35led != 'RX/TX BLINKING' :
         f=3
         cursor.execute("update dscndaily set V35_LED = %s where dscndaily_id = %s",[v35led,id])
         remarks = "Rx/Tx -not Blinking(update)"
         val = (emp_id,remarks,v35led,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set V35_LED = %s where dscndaily_id = %s",[v35led,id])
            
     if aled != 'OFF' :
         f=3
         cursor.execute("update dscndaily set Alarm_LED = %s where dscndaily_id = %s",[aled,id])
         remarks = "Alarm LED was turned ON(update)"
         val = (emp_id,remarks,aled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set Alarm_LED = %s where dscndaily_id = %s",[aled,id])
          
     if int(iv) < 220 or int(iv) > 240 :
         f=3
         cursor.execute("update dscndaily set IP_Voltage = %s where dscndaily_id = %s",[iv,id])
         remarks = "UPS I/P Voltage exceeding normal voltage(update)"
         val = (emp_id,remarks,iv,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set IP_Voltage = %s where dscndaily_id = %s",[iv,id])
        
     if int(ov) < 220 or int(ov) > 240 :
         f=3
         cursor.execute("update dscndaily set OP_voltage = %s where dscndaily_id = %s",[iv,id])
         remarks = "UPS O/P Voltage exceeding normal voltage(update)"
         val = (emp_id,remarks,ov,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set OP_voltage = %s where dscndaily_id = %s",[iv,id])
     
     if int(bv) < 180 or int(bv) > 250 :
         f=3
         cursor.execute("update dscndaily set Battery_voltage = %s where dscndaily_id = %s",[bv,id])
         remarks = "UPS Battery Voltage exceeding normal voltage(update)"
         val = (emp_id,remarks,bv,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set Battery_voltage = %s where dscndaily_id = %s",[bv,id])
         
     if  cof != 'OK' :
         f=3
         cursor.execute("update dscndaily set CorO_Function = %s where dscndaily_id = %s",[cof,id])
         remarks = "C/O Function not OK(update)"
         val = (emp_id,remarks,cof,currdate,currtime)
         sql = "INSERT INTO vhfdlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set CorO_Function = %s where dscndaily_id = %s",[cof,id])
          
     if ioled == 'STEADY ON' and pwled == 'STEADY ON' and oled == 'STEADY ON' and v35led == 'RX/TX BLINKING' and aled == 'OFF' and sled == 'STEADY ON' and cof == 'OK' and (int(bv) > 179 and int(bv) < 251) and (int(ov) > 219 and int(ov) < 241) and (int(iv) > 219 and int(iv) < 241) :
          uincharappro = "YES"
          f=1
          remarks = "Parameter/s fixed"
          value = "All parameters NORMAL"
          val = (emp_id,remarks,value,currdate,currtime)
          sql = "INSERT INTO dscndlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
          cursor.execute(sql,val)
          cursor.execute("update dscndaily set Unit_Incharge_Approval = %s where dscndaily_id = %s",[uincharappro,id])
          cursor.execute("update dscndaily set Remarks = %s where dscndaily_id = %s",[rmarks,id])
     
     dscn_d = models.Dscndaily.objects.all()
     dscn_d = dscn_d.values('dscndaily_id','date','time','sat_led','odu_led','io_led','alarm_led','power_led','v35_led','ip_voltage','op_voltage','battery_voltage','coro_function','remarks','unit_incharge_approval')
     return render(request,'engineer/dscn/dscndailyrep.html',{'dscn_d':dscn_d,'id':emp_id,'flag':f})
      
       