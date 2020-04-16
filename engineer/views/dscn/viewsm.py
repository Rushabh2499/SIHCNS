from django.shortcuts import render
from django.db import connection
from datetime import date,datetime
# Create your views here.
from login import models as models

def dscnmonthlylogs(request, id):
  if request.session.has_key('uid'):
     dscn_m = models.Dscnmonthly.objects.all()
     dscn_m = dscn_m.values('dscnmonthly_id','date','time','cleaning_dscn_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check','remarks','unit_incharge_approval')
     dscn_m = dscn_m.filter(emp_id=id)
     f=1
     return render(request,'engineer/dscn/dscnmonrep.html',{'dscn_m':dscn_m,'id':id,'f':f}) 
  else : 
     return render(request,'login/login.html')
 
def dscnm(request, id) :
  if request.session.has_key('uid'):
     dscn_m = models.Dscnmonthly.objects.all()
     dscn_m = dscn_m.values('dscnmonthly_id','date','time','cleaning_dscn_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check','remarks','unit_incharge_approval')
     dscn_m = dscn_m.filter(emp_id=id)
     f=0
     return render(request,'engineer/dscn/dscnmonrep.html',{'dscn_m':dscn_m,'id':id,'f':f}) 
  else : 
     return render(request,'login/login.html')

def dscnmrep(request, id) :
   return render(request,'engineer/dscn/dscnmrepsub.html',{'id':id}) 
     
def dscnmrepsub(request, id):
   a_id = models.Engineer.objects.all()
   a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id'] 
   currtime = datetime.now().strftime("%H:%M:%S")
   emp_id = models.Vhfmonthly.objects.all()
   emp_id = emp_id.values('emp_id').filter(emp_id=id)[0]['emp_id']
   currdate= date.today()
   cursor = connection.cursor() 
   cdae = request.POST['cdae']
   bbt = request.POST['bbt']
   ubvl = request.POST['ubvl']
   ancc = request.POST['ancc']
   er=request.POST['er']
   ev = request.POST['ev']
   esac=request.POST['esac']
   remarks=request.POST['remarks']
   sql = "INSERT INTO dscnmonthly (date,time,a_id,emp_id,f_id,Cleaning_DSCN_associated_eqpt,Battery_backup_time_of_UPS1nUPS2,UPS_battery_voltage_on_load,Antenna_n_cable_check,Earth_resistance,EorN_voltage,eqpt_status_after_check,REMARKS,Unit_incharge_approval) VALUES (%s, %s,%s,%s,%s, %s, %s, %s, %s,%s, %s,%s,%s,%s, %s, %s, %s, %s)"
   val = (currdate,currtime,a_id,id,'3',cdae,bbt,ubvl,ancc,er,ev,esac,remarks,"YES")
   cursor.execute(sql, val)
   dscn_m = models.Dscnmonthly.objects.all()
   dscn_m = dscn_m.values('dscnmonthly_id','date','time','cleaning_dscn_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check','remarks','unit_incharge_approval')
   dscn_m = dscn_m.filter(emp_id=id)
   f = 0
   return render(request,'engineer/dscn/dscnmonrep.html',{'dscn_m':dscn_m,'id':id,'f':f}) 
       
def editdscnmonthly(request, dscnmonthly_id):
   cursor = connection.cursor() 
   dscnm = models.Dscnmonthly.objects.all()
   dscnm = dscnm.values('dscnmonthly_id','date','time','emp_id','cleaning_dscn_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check','remarks','unit_incharge_approval')
   dscnm = dscnm.filter(dscnmonthly_id=dscnmonthly_id)
   dscn_id = dscnm.values('dscnmonthly_id').filter(dscnmonthly_id=dscnmonthly_id)[0]['dscnmonthly_id']
   return render(request,'engineer/vhf/editdscnmrepsub.html',{'dscnm':dscnm,'id':dscn_id})

def updscnmonthly(request, id):
   cursor = connection.cursor() 
   currtime = datetime.now().strftime("%H:%M:%S")
   emp_id = models.Dscnmonthly.objects.all()
   emp_id = emp_id.values('emp_id').filter(dscnmonthly_id=id)[0]['emp_id']
   currdate= date.today()
   cdae = request.POST['cdae']
   bbt = request.POST['bbt']
   ubvl = request.POST['ubvl']
   ancc = request.POST['ancc']
   er=request.POST['er']
   ev = request.POST['ev']
   esac=request.POST['esac']
   remarks=request.POST['remarks']
   cursor.execute("update dscnmonthly set Cleaning_DSCN_associated_eqpt = %s where dscnmonthly_id = %s",[cdae,id]) 
   cursor.execute("update dscnmonthly set Antenna_n_Cable_check = %s where dscnmonthly = %s",[ancc,id]) 
   cursor.execute("update dscnmonthly set REMARKS = %s where dscnmonthly = %s",[remarks,id]) 
   cursor.execute("update dscnmonthly set Battery_backup_time_of_UPS1nUPS2 = %s where dscnmonthly = %s",[bbt,id]) 
   cursor.execute("update dscnmonthly set UPS_battery_voltage_on_load = %s where dscnmonthly = %s",[ubvl,id]) 
   cursor.execute("update dscnmonthly set Earth_resistance = %s where dscnmonthly = %s",[er,id]) 
   cursor.execute("update dscnmonthly set EorN_voltage = %s where dscnmonthly = %s",[ev,id]) 
   cursor.execute("update dscnmonthly set eqpt_status_after_check = %s where dscnmonthly = %s",[esac,id]) 
   
   dscn_m = dscn_m.values('dscnmonthly_id','date','time','cleaning_dscn_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check','remarks','unit_incharge_approval')
   dscn_m = dscn_m.filter(emp_id=id)
   f = 0
   return render(request,'engineer/dscn/dscnmonrep.html',{'dscn_m':dscn_m,'id':emp_id,'f':f}) 
             