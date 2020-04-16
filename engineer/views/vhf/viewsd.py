from django.shortcuts import render
from django.db import connection
from datetime import date,datetime,timedelta
# Create your views here.
from login import models as models
from engineer.views.datis.viewsd import routebackdatisd 
def routebackvhfd(request , id):
   return routebackdatisd(request,id)

def vhfdlogs(request, id) :
   if request.session.has_key('uid'):
     vhf_d = models.Vhfdaily.objects.all()
     vhf_d = vhf_d.values('vhfdaily_id','date','time','rx_no','frequency_mhz','bit_test','status','rxn_check','sq_threshold','unit_incharge_approval')
     vhf_d = vhf_d.filter(emp_id=id)
     f=1
     return render(request,'engineer/vhf/vhfdailyrep.html',{'vhf_d':vhf_d,'id':id,'f':f})
   else : 
     return render(request,'login/login.html')
 
def vhfdailyrec(request, id):
   if request.session.has_key('uid'):
     vhf_d = models.Vhfdaily.objects.all()
     vhf_d = vhf_d.values('vhfdaily_id','date','time','rx_no','frequency_mhz','bit_test','status','rxn_check','sq_threshold','unit_incharge_approval')
     vhf_d = vhf_d.filter(emp_id=id)
     f=0
     return render(request,'engineer/vhf/vhfdailyrep.html',{'vhf_d':vhf_d,'id':id,'f':f})
   else : 
     return render(request,'login/login.html')


def vhfd(request, id) :
   if request.session.has_key('uid'):
     vhf_d = models.Vhfdaily.objects.all()
     vhf_d = vhf_d.values('vhfdaily_id','date','time','rx_no','frequency_mhz','bit_test','status','rxn_check','sq_threshold','unit_incharge_approval')
     vhf_d = vhf_d.filter(emp_id=id)
     f=0
     return render(request,'engineer/vhf/vhfdailyrep.html',{'vhf_d':vhf_d,'id':id,'f':f})
   else : 
     return render(request,'login/login.html')

def vhfdrep(request, id) :
     return render(request,'engineer/vhf/vhfrepsub.html',{'id':id})      

def vhfdrepsub(request, id) :
    cursor = connection.cursor()
    currdate= date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    a_id = models.Engineer.objects.all()
    a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id']
    rxno=''
    freqmhz=''
    bittest=''
    status=''
    rxncheck=''
    sqthreshold=''
    uincharappro=''
    rxno=request.POST['RX_No']
    freqmhz = request.POST['Frequency_MHZ']
    bittest = request.POST['Bit_Status']
    if bittest != 'PASS' :
         remarks = "Bit test failed"
         val = (id,remarks,bittest,currdate,currtime)
         sql = "INSERT INTO vhfdlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
         
    status = request.POST['Status']
    if status != 'READY' :
         remarks = "Not Ready"
         val = (id,remarks,status,currdate,currtime)
         sql = "INSERT INTO vhfdlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
    rxncheck=request.POST['RXN_Check']
    if rxncheck != 'RXN NORMAL' :
         remarks = "RXN_Check not normal"
         val = (id,remarks,rxncheck,currdate,currtime)
         sql = "INSERT INTO vhfdlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
    sqthreshold=request.POST['SQ_Threshold']
    if  int(sqthreshold) < -80 :
         remarks = "SQ Threshold above -80 Db"
         val = (id,remarks,sqthreshold,currdate,currtime)
         sql = "INSERT INTO vhfdlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
    
    if bittest == 'PASS' and status == 'READY' and rxncheck == 'RXN NORMAL' and int(sqthreshold) < -80 :
          uincharappro = "YES"
          f=1
    else :
          f=2
          uincharappro = "NO"      
 
    sql = "INSERT INTO vhfdaily (date,time,emp_id,a_id,RX_no,frequency_MHz,bit_test,status,RXN_check,SQ_threshold,Unit_Incharge_Approval) VALUES (%s, %s,%s,%s,%s, %s, %s, %s, %s,%s,%s)"
    val = (currdate,currtime,id,a_id,rxno,freqmhz,bittest,status,rxncheck,sqthreshold,uincharappro)
    cursor.execute(sql, val)
    vhf_d = models.Vhfdaily.objects.all()
    vhf_d = vhf_d.values('vhfdaily_id','date','time','rx_no','frequency_mhz','bit_test','status','rxn_check','sq_threshold','unit_incharge_approval')
    cdate = cursor.execute("select date from vhfdaily where date = %s",[currdate])    
    return render(request,'engineer/vhf/vhfdailyrep.html',{'vhf_d':vhf_d,'id':id,'flag':f})

def editvhfdaily(request,vhfdaily_id) :
    cursor = connection.cursor() 
    vhf_d = models.Vhfdaily.objects.all()
    vhf_d = vhf_d.values('vhfdaily_id','date','time','emp_id','rx_no','frequency_mhz','bit_test','status','rxn_check','sq_threshold','unit_incharge_approval')
    vhfd = vhf_d.filter(vhfdaily_id=vhfdaily_id)
    vhfd_id = vhfd.values('vhfdaily_id').filter(vhfdaily_id=vhfdaily_id)[0]['vhfdaily_id']
    return render(request,'engineer/vhf/editvhfrepsub.html',{'vhfd':vhfd,'id':vhfd_id}) 
   
def upvhfdaily(request, id) :
    cursor = connection.cursor() 
    currtime = datetime.now().strftime("%H:%M:%S")
    emp_id = models.Vhfdaily.objects.all()
    emp_id = emp_id.values('emp_id').filter(vhfdaily_id=id)[0]['emp_id']
    currdate= date.today()
    rxno=''
    freqmhz=''
    bittest=''
    status=''
    rxncheck=''
    sqthreshold=''
    uincharappro=''
    rxno=request.POST['RX_No']
    freqmhz = request.POST['Frequency_MHZ']
    bittest = request.POST['Bit_Status']
    
    if bittest != 'PASS' :
       remarks = "Bit test failed(update)"
       cursor.execute("update vhfdaily set bit_test = %s where vhfdaily_id = %s",[bittest,id])
       val = (emp_id,remarks,bittest,currdate,currtime)
       sql = "INSERT INTO vhfdlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
       cursor.execute(sql,val) 
    else :
       cursor.execute("update vhfdaily set bit_test = %s where vhfdaily_id = %s",[bittest,id])
            
    status = request.POST['Status']
    if status != 'READY' :
         remarks = "Not Ready(update)"
         cursor.execute("update vhfdaily set status = %s where vhfdaily_id = %s",[status,id])
         val = (emp_id,remarks,status,currdate,currtime)
         sql = "INSERT INTO vhfdlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
    else :
         cursor.execute("update vhfdaily set status = %s where vhfdaily_id = %s",[status,id])
              
    rxncheck=request.POST['RXN_Check']
    if rxncheck != 'RXN NORMAL' :
         remarks = "RXN_Check not normal(update)"
         cursor.execute("update vhfdaily set RXN_check = %s where vhfdaily_id = %s",[rxncheck,id])
         val = (emp_id,remarks,rxncheck,currdate,currtime)
         sql = "INSERT INTO vhfdlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
    else :
         cursor.execute("update vhfdaily set RXN_check = %s where vhfdaily_id = %s",[rxncheck,id])
          
    sqthreshold=request.POST['SQ_Threshold']
    if  int(sqthreshold) < -80 :
         cursor.execute("update vhfdaily set SQ_threshold = %s where vhfdaily_id = %s",[sqthreshold,id])
         remarks = "SQ Threshold above -80 Db(update)"
         val = (emp_id,remarks,sqthreshold,currdate,currtime)
         sql = "INSERT INTO vhfdlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
    else :   
         cursor.execute("update vhfdaily set SQ_threshold = %s where vhfdaily_id = %s",[sqthreshold,id])
          
    if bittest == 'PASS' and status == 'READY' and rxncheck == 'RXN NORMAL' and int(sqthreshold) < -80 :
          uincharappro = "YES"
          f=1
          remarks = "Parameter/s fixed"
          value = "All parameters NORMAL"
          val = (emp_id,remarks,value,currdate,currtime)
          sql = "INSERT INTO vhfdlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
          cursor.execute(sql,val)
          cursor.execute("update vhfdaily set bit_test = %s where vhfdaily_id = %s",[bittest,id])
          cursor.execute("update vhfdaily set status = %s where vhfdaily_id = %s",[status,id])
          cursor.execute("update vhfdaily set RXN_check = %s where vhfdaily_id = %s",[rxncheck,id])
          cursor.execute("update vhfdaily set SQ_threshold = %s where vhfdaily_id = %s",[sqthreshold,id])
          cursor.execute("update vhfdaily set Unit_Incharge_Approval = %s where vhfdaily_id = %s",[uincharappro,id])
          
    vhf_d = models.Vhfdaily.objects.all()
    vhf_d = vhf_d.values('vhfdaily_id','date','time','rx_no','frequency_mhz','bit_test','status','rxn_check','sq_threshold','unit_incharge_approval')
    vhfd = vhf_d.filter(vhfdaily_id=id)
    vhfd = vhfd.values('vhfdaily_id').filter(vhfdaily_id=id)[0]['vhfdaily_id']
    currdate= date.today()
    cdate = cursor.execute("select date from vhfdaily where date = %s",[currdate])    
    f=0
    if bittest == 'PASS' and status == 'READY' and rxncheck == 'RXN NORMAL' and int(sqthreshold) < -80 :
         f=1
    else :
         f=2 
    return render(request,'engineer/vhf/vhfdailyrep.html',{'vhf_d':vhf_d,'id':emp_id,'flag':f})
         
