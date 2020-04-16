from django.shortcuts import render
from django.db import connection
from datetime import date,datetime,timedelta
# Create your views here.
from login import models as models

def vhfylogs(request, id) :
   if request.session.has_key('uid'):
     vhf_y = models.Vhfyearly.objects.all()
     vhf_y = vhf_y.values('vhfyearly_id','date','time','rx_no','frequency_mhz','reference_freq','power','bit_test','ac_dc_changeover','remarks','unit_incharge_approval')
     vhf_y = vhf_y.filter(emp_id=id)
     f=1
     return render(request,'engineer/vhf/vhfyearrep.html',{'vhf_y':vhf_y,'id':id,'f':f}) 
   else: 
     return render(request,'login/login.html')

def vhfy(request, id) :
   if request.session.has_key('uid'):
     vhf_y = models.Vhfyearly.objects.all()
     vhf_y = vhf_y.values('vhfyearly_id','date','time','rx_no','frequency_mhz','reference_freq','power','bit_test','ac_dc_changeover','remarks','unit_incharge_approval')
     vhf_y = vhf_y.filter(emp_id=id)
     f=0
     return render(request,'engineer/vhf/vhfyearrep.html',{'vhf_y':vhf_y,'id':id,'f':f}) 
   else: 
     return render(request,'login/login.html')

def vhfyrep(request, id) :
     return render(request,'engineer/vhf/vhfyrepsub.html',{'id':id})

def vhfyrepsub(request,id) :
     cursor = connection.cursor()
     currdate= date.today()
     currtime = datetime.now().strftime("%H:%M:%S")
     a_id = models.Engineer.objects.all()
     a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id']
     fm = request.POST['fm']
     rf=request.POST['rf']
     pw = request.POST['pw']
     bt = request.POST['bt']
     acdc = request.POST['acdc']
     remarks = request.POST['remarks']
     f=2
     if float(rf) != 20.95 :
          f=3
          remarks = "Reference Frequency not correct"
          val = (id,remarks,rf,currdate,currtime)
          sql = "INSERT INTO vhfylogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
          cursor.execute(sql,val)
         
     if int(pw) < 10 and int(pw) > 50 :
          f=3
          remarks = "Power not in range"
          val = (id,remarks,pw,currdate,currtime)
          sql = "INSERT INTO vhfylogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
          cursor.execute(sql,val)
     
     if bt != 'PASS' :
          f=3
          remarks = "Bit Test failed"
          val = (id,remarks,bt,currdate,currtime)
          sql = "INSERT INTO vhfylogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
          cursor.execute(sql,val)
     
     if  acdc != 'NORMAL(DC)'  :
          f=3
          remarks = "AC/DC Changeover not normal"
          val = (id,remarks,acdc,currdate,currtime)
          sql = "INSERT INTO vhfylogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
          cursor.execute(sql,val)
    
     if float(rf) == 20.95 and (int(pw) > 9 and int(pw) < 51) and bt == 'PASS'and acdc == 'NORMAL(DC)' :
          uincharappro = "YES"
          f=1
     else :
          f=3
          uincharappro = "NO"      
 
     sql = "INSERT INTO vhfyearly (date,time,emp_id,a_id,frequency_MHz,reference_freq,power,bit_test,AC_DC_changeover,remarks,Unit_incharge_approval) VALUES (%s, %s,%s,%s,%s, %s, %s, %s, %s,%s,%s)"
     val = (currdate,currtime,id,a_id,fm,rf,pw,bt,acdc,remarks,uincharappro)
     cursor.execute(sql, val)
     vhf_y = models.Vhfyearly.objects.all()
     vhf_y = vhf_y.values('vhfyearly_id','date','time','rx_no','frequency_mhz','reference_freq','power','bit_test','ac_dc_changeover','remarks','unit_incharge_approval')
     return render(request,'engineer/vhf/vhfyearrep.html',{'vhf_y':vhf_y,'id':id,'flag':f})

def editvhfyearly(request,vhfyearly_id) :
     cursor = connection.cursor() 
     vhfy = models.Vhfyearly.objects.all()
     vhfy = vhfy.values('vhfyearly_id','date','time','emp_id','rx_no','frequency_mhz','reference_freq','power','bit_test','ac_dc_changeover','remarks','unit_incharge_approval')
     vhfy = vhfy.filter(vhfyearly_id=vhfyearly_id)
     vhf_id = vhfy.values('vhfyearly_id').filter(vhfyearly_id=vhfyearly_id)[0]['vhfyearly_id']
     return render(request,'engineer/vhf/editvhfyrepsub.html',{'vhfy':vhfy,'id':vhf_id})

def upvhfyearly(request, id) :
     cursor = connection.cursor() 
     currtime = datetime.now().strftime("%H:%M:%S")
     emp_id = models.Vhfyearly.objects.all()
     emp_id = emp_id.values('emp_id').filter(vhfyearly_id=id)[0]['emp_id']
     currdate= date.today()
     fm = request.POST['fm']
     rf=request.POST['rf']
     pw = request.POST['pw']
     bt = request.POST['bt']
     acdc = request.POST['acdc']
     remarks = request.POST['remarks']
     f=2
     if float(rf) != 20.95 :
          f=3
          cursor.execute("update vhfyearly set reference_freq = %s where vhfyearly_id = %s",[rf,id])
          remarks = "Reference Frequency not correc(update)"
          val = (emp_id,remarks,rf,currdate,currtime)
          sql = "INSERT INTO vhfylogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
          cursor.execute(sql,val)
     else :
          cursor.execute("update vhfyearly set reference_freq = %s where vhfyearly_id = %s",[rf,id])
         
     if int(pw) < 10 and int(pw) > 50 :
          f=3
          cursor.execute("update vhfyearly set power = %s where vhfyearly_id = %s",[pw,id])
          remarks = "Power not in range(update)"
          val = (emp_id,remarks,pw,currdate,currtime)
          sql = "INSERT INTO vhfylogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
          cursor.execute(sql,val)
     else :
          cursor.execute("update vhfyearly set power = %s where vhfyearly_id = %s",[pw,id])
       
     if bt != 'PASS' :
          f=3
          cursor.execute("update vhfyearly set bit_test = %s where vhfyearly_id = %s",[bt,id])
          remarks = "Bit Test failed(update)"
          val = (emp_id,remarks,bt,currdate,currtime)
          sql = "INSERT INTO vhfylogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
          cursor.execute(sql,val)
     else :
          cursor.execute("update vhfyearly set bit_test = %s where vhfyearly_id = %s",[bt,id])
     
     if  acdc != 'NORMAL(DC)'  :
          f=3
          cursor.execute("update vhfyearly set AC_DC_changeover = %s where vhfyearly_id = %s",[acdc,id])
          remarks = "AC/DC Changeover not normal(update)"
          val = (emp_id,remarks,acdc,currdate,currtime)
          sql = "INSERT INTO vhfylogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
          cursor.execute(sql,val)
     else :
          cursor.execute("update vhfyearly set AC_DC_changeover = %s where vhfyearly_id = %s",[acdc,id]) 

     if float(rf) == 20.95 and (int(pw) > 9 and int(pw) < 51) and bt == 'PASS'and acdc == 'NORMAL(DC)' :
          uincharappro = "YES"
          f=2
          remarks = "Parameter/s fixed"
          value = "All parameters NORMAL"
          val = (emp_id,remarks,value,currdate,currtime)
          sql = "INSERT INTO vhfylogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
          cursor.execute(sql,val)
          cursor.execute("update vhfyearly set reference_freq = %s where vhfyearly_id = %s",[rf,id])
          cursor.execute("update vhfyearly set power = %s where vhfyearly_id = %s",[pw,id])
          cursor.execute("update vhfyearly set bit_test = %s where vhfyearly_id = %s",[bt,id])
          cursor.execute("update vhfyearly set AC_DC_changeover = %s where vhfyearly_id = %s",[acdc,id]) 
          cursor.execute("update vhfyearly set Remarks = %s where vhfyearly_id = %s",[remarks,id]) 
          cursor.execute("update vhfyearly set Unit_incharge_approval = %s where vhfyearly_id = %s",[uincharappro,id]) 

     vhf_y = models.Vhfyearly.objects.all()
     vhf_y = vhf_y.values('vhfyearly_id','date','time','rx_no','frequency_mhz','reference_freq','power','bit_test','ac_dc_changeover','remarks','unit_incharge_approval')
     return render(request,'engineer/vhf/vhfyearrep.html',{'vhf_y':vhf_y,'id':emp_id,'flag':f})
         

