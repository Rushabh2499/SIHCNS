from django.shortcuts import render
from django.db import connection
from datetime import date,datetime,timedelta
# Create your views here.
from login import models as models

def vhfmlogs(request , id) :
  if request.session.has_key('uid'):
    vhf_m = models.Vhfmonthly.objects.all()
    vhf_m = vhf_m.values('vhfmonthly_id','date','time','modulation_mode','line_op','squelch_defeat','squelch_threshold','squelch_carrier_override','rf_pre_attn','agc','ready_signal','squelch_op_marc','squelch_op_facilities','squelch_op_phantom','squelch_defeat_ip','bit_test','unit_incharge_approval')
    vhf_m = vhf_m.filter(emp_id=id)
    f=1
    return render(request,'engineer/vhf/vhfmonrep.html',{'vhf_m':vhf_m,'id':id,'f':f}) 
  else : 
     return render(request,'login/login.html')

def vhfm(request, id) :
  if request.session.has_key('uid'):
    vhf_m = models.Vhfmonthly.objects.all()
    vhf_m = vhf_m.values('vhfmonthly_id','date','time','modulation_mode','line_op','squelch_defeat','squelch_threshold','squelch_carrier_override','rf_pre_attn','agc','ready_signal','squelch_op_marc','squelch_op_facilities','squelch_op_phantom','squelch_defeat_ip','bit_test','unit_incharge_approval')
    vhf_m = vhf_m.filter(emp_id=id)
    f=0
    return render(request,'engineer/vhf/vhfmonrep.html',{'vhf_m':vhf_m,'id':id,'f':f}) 
  else : 
     return render(request,'login/login.html')

def vhfmrep(request, id) :
    return render(request,'engineer/vhf/vhfmrepsub.html',{'id':id}) 

def vhfmrepsub(request, id) :
    a_id = models.Engineer.objects.all()
    a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id'] 
    currtime = datetime.now().strftime("%H:%M:%S")
    emp_id = models.Vhfmonthly.objects.all()
    emp_id = emp_id.values('emp_id').filter(emp_id=id)[0]['emp_id']
    currdate= date.today()
    cursor = connection.cursor() 
    mm = request.POST['modulation mode']
    lop = request.POST['line op']
    sqd = request.POST['squelch defeat']
    sqt=request.POST['squelch threshold']
    sco=request.POST['squelch carrier override']
    rpattn=request.POST['RF pre ATTN']
    agc=request.POST['AGC']
    rs=request.POST['Ready signal']
    som=request.POST['Squelch op marc']
    sof=request.POST['Squelch op facilities']
    sop=request.POST['Squelch op phantom']
    sdi=request.POST['Squelch defeat ip']
    bittest=request.POST['bit test']
    f=2
    if mm != 'AM-Voice' and mm != 'FM-Voice' and mm != 'PM-Voice' :  
            f=3
            remarks = "Incorrent Value for mode modulation"
            val = (id,remarks,mm,currdate,currtime)
            sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
            cursor.execute(sql,val)
    
    if int(lop) > 13 :
        f=3
        remarks = "Line of input above 13dbm"
        val = (id,remarks,lop,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
        
    if sqd != 'OFF' :
        f=3
        remarks = "Squelch Default is not off"
        val = (id,remarks,sqd,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    
    if int(sqt) < -115 :
        f=3
        remarks = "Squelch Threshold not normal "
        val = (id,remarks,sqt,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val) 
    
    if sco != 'OFF' :
        f=3
        remarks = "Squelch carrier Override is not off"
        val = (id,remarks,sco,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    
    if rpattn != 'OFF' :
        f=3
        remarks = "RF PRE ATTN is not off"
        val = (id,remarks,rpattn,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    if agc != 'ON' :
        f=3
        remarks = "AGC is not On"
        val = (id,remarks,agc,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    
    if rs != 'STD' :
        f=3
        remarks = "Ready signal not standard"
        val = (id,remarks,rs,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    
    if som != 'STD' :
        f=3
        remarks = "SQUELCH O/P-MARC not standard"
        val = (id,remarks,som,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    if sof != 'STD' :
        f=3
        remarks = "SQUELCH O/P FACILITIES not standard"
        val = (id,remarks,sof,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    if sop != 'STD' :
        f=3
        remarks = "SQUELCH O/P PHANTOM not standard"
        val = (id,remarks,sop,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    if sdi != 'STD' :
        f=3
        remarks = "SQUELCH DEFEAT I/P not standard"
        val = (id,remarks,sdi,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    if bittest != 'OK' :
        f=3
        remarks = "Bit test not OK"
        val = (id,remarks,bittest,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
   
    uiapp = "NO"
    print(f)
    if f == 2 :
         uiapp = "YES"
    sql = "INSERT INTO vhfmonthly (date,time,emp_id,a_id,modulation_mode,line_op,squelch_defeat,squelch_threshold,squelch_carrier_override,RF_pre_ATTN,AGC,Ready_signal,Squelch_op_marc,Squelch_op_facilities,Squelch_op_phantom,Squelch_defeat_ip,bit_test,Unit_incharge_approval) VALUES (%s, %s,%s,%s,%s, %s, %s, %s, %s,%s, %s,%s,%s,%s, %s, %s, %s, %s)"
    val = (currdate,currtime,id,a_id,mm,lop,sqd,sqt,sco,rpattn,agc,rs,som,sof,sop,sdi,bittest,uiapp)
    cursor.execute(sql, val)
    vhf_m = models.Vhfmonthly.objects.all()
    vhf_m = vhf_m.values('vhfmonthly_id','date','time','modulation_mode','line_op','squelch_defeat','squelch_threshold','squelch_carrier_override','rf_pre_attn','agc','ready_signal','squelch_op_marc','squelch_op_facilities','squelch_op_phantom','squelch_defeat_ip','bit_test','unit_incharge_approval')
    vhf_m = vhf_m.filter(emp_id=id)
    return render(request,'engineer/vhf/vhfmonrep.html',{'vhf_m':vhf_m,'id':id,'flag':f}) 
   
def editvhfmonthly(request,vhfmonthly_id) :
    cursor = connection.cursor() 
    vhfm = models.Vhfmonthly.objects.all()
    vhfm = vhfm.values('vhfmonthly_id','date','time','emp_id','modulation_mode','line_op','squelch_defeat','squelch_threshold','squelch_carrier_override','rf_pre_attn','agc','ready_signal','squelch_op_marc','squelch_op_facilities','squelch_op_phantom','squelch_defeat_ip','bit_test','unit_incharge_approval')
    vhfm = vhfm.filter(vhfmonthly_id=vhfmonthly_id)
    vhf_id = vhfm.values('vhfmonthly_id').filter(vhfmonthly_id=vhfmonthly_id)[0]['vhfmonthly_id']
    return render(request,'engineer/vhf/editvhfmrepsub.html',{'vhfm':vhfm,'id':vhf_id})

def upvhfmonthly(request, id) :
    currtime = datetime.now().strftime("%H:%M:%S")
    emp_id = models.Vhfmonthly.objects.all()
    emp_id = emp_id.values('emp_id').filter(vhfmonthly_id=id)[0]['emp_id']
    currdate= date.today()
    cursor = connection.cursor() 
    mm = request.POST['modulation mode']
    lop = request.POST['line op']
    sqd = request.POST['squelch defeat']
    sqt=request.POST['squelch threshold']
    sco=request.POST['squelch carrier override']
    rpattn=request.POST['RF pre ATTN']
    agc=request.POST['AGC']
    rs=request.POST['Ready signal']
    som=request.POST['Squelch op marc']
    sof=request.POST['Squelch op facilities']
    sop=request.POST['Squelch op phantom']
    sdi=request.POST['Squelch defeat ip']
    bittest=request.POST['bit test']
    f=2
    if mm != 'AM-Voice' and mm != 'FM-Voice' and mm != 'PM-Voice' :  
        f=3
        cursor.execute("update vhfmonthly set modulation_mode = %s where vhfmonthly_id = %s",[mm,id])
        remarks = "Incorrent Value for mode modulation(update)"
        val = (emp_id,remarks,mm,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :   
        cursor.execute("update vhfmonthly set modulation_mode = %s where vhfmonthly_id = %s",[mm,id])
        
    if int(lop) > 13 :
        f=3
        cursor.execute("update vhfmonthly set line_op = %s where vhfmonthly_id = %s",[lop,id])
        remarks = "Line of input above 13dbm"
        val = (emp_id,remarks,lop,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update vhfmonthly set line_op = %s where vhfmonthly_id = %s",[lop,id])
       
    if sqd != 'OFF' :
        f=3
        cursor.execute("update vhfmonthly set squelch_defeat = %s where vhfmonthly_id = %s",[sqd,id])
        remarks = "Squelch Default is not off(update)"
        val = (emp_id,remarks,sqd,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update vhfmonthly set squelch_defeat = %s where vhfmonthly_id = %s",[sqd,id])
        
    if int(sqt) < -115 :
        f=3
        cursor.execute("update vhfmonthly set squelch_threshold = %s where vhfmonthly_id = %s",[sqt,id])
        remarks = "Squelch Threshold not normal "
        val = (emp_id,remarks,sqt,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val) 
    else :
        cursor.execute("update vhfmonthly set squelch_threshold = %s where vhfmonthly_id = %s",[sqt,id])
        
    if sco != 'OFF' :
        f=3
        cursor.execute("update vhfmonthly set squelch_carrier_override = %s where vhfmonthly_id = %s",[sco,id])
        remarks = "Squelch carrier Override is not off(update)"
        val = (emp_id,remarks,sco,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update vhfmonthly set squelch_carrier_override = %s where vhfmonthly_id = %s",[sco,id])
         
    if rpattn != 'OFF' :
        f=3
        cursor.execute("update vhfmonthly set RF_pre_ATTN = %s where vhfmonthly_id = %s",[rpattn,id])
        remarks = "RF PRE ATTN is not off(update)"
        val = (emp_id,remarks,rpattn,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update vhfmonthly set RF_pre_ATTN = %s where vhfmonthly_id = %s",[rpattn,id])
        
    if agc != 'ON' :
        f=3
        cursor.execute("update vhfmonthly set AGC = %s where vhfmonthly_id = %s",[agc,id])
        remarks = "AGC is not On(update)"
        val = (emp_id,remarks,agc,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update vhfmonthly set AGC = %s where vhfmonthly_id = %s",[agc,id])
    
    if rs != 'STD' :
        f=3
        cursor.execute("update vhfmonthly set Ready_signal = %s where vhfmonthly_id = %s",[rs,id])
        remarks = "Ready signal not standard(update)"
        val = (emp_id,remarks,rs,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update vhfmonthly set Ready_signal = %s where vhfmonthly_id = %s",[rs,id])
     
    if som != 'STD' :
        f=3
        cursor.execute("update vhfmonthly set Squelch_op_marc = %s where vhfmonthly_id = %s",[som,id])
        remarks = "SQUELCH O/P-MARC not standard(update)"
        val = (emp_id,remarks,som,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update vhfmonthly set Squelch_op_marc = %s where vhfmonthly_id = %s",[som,id])
    if sof != 'STD' :
        f=3
        cursor.execute("update vhfmonthly set Squelch_op_facilities = %s where vhfmonthly_id = %s",[sof,id])
        remarks = "SQUELCH O/P FACILITIES not standard(update)"
        val = (emp_id,remarks,sof,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update vhfmonthly set Squelch_op_facilities = %s where vhfmonthly_id = %s",[sof,id])
        
    if sop != 'STD' :
        f=3
        cursor.execute("update vhfmonthly set Squelch_op_phantom = %s where vhfmonthly_id = %s",[sop,id])
        remarks = "SQUELCH O/P PHANTOM not standard(update)"
        val = (emp_id,remarks,sop,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update vhfmonthly set Squelch_op_phantom = %s where vhfmonthly_id = %s",[sop,id])
    
    if sdi != 'STD' :
        f=3
        cursor.execute("update vhfmonthly set Squelch_defeat_ip = %s where vhfmonthly_id = %s",[sdi,id])
        remarks = "SQUELCH DEFEAT I/P not standard(update)"
        val = (emp_id,remarks,sdi,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update vhfmonthly set Squelch_defeat_ip = %s where vhfmonthly_id = %s",[sdi,id])
         
    if bittest != 'OK' :
        f=3
        cursor.execute("update vhfmonthly set bit_test = %s where vhfmonthly_id = %s",[bittest,id])
        remarks = "Bit test not OK(update)"
        val = (emp_id,remarks,bittest,currdate,currtime)
        sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update vhfmonthly set bit_test = %s where vhfmonthly_id = %s",[bittest,id])
         
    if (mm == 'AM-Voice' or mm == 'FM-Voice' or mm == 'PM-Voice') and int(lop) < 13 and int(sqt) > -115 and sqd == 'OFF' and sco == 'OFF' and rpattn == 'OFF' and agc == 'ON' and rs == 'STD' and som == 'STD' and sof == 'STD' and sop == 'STD' and sdi == 'STD' and bittest == 'OK' : 
       cursor.execute("update vhfmonthly set bit_test = %s where vhfmonthly_id = %s",[bittest,id])
       cursor.execute("update vhfmonthly set Squelch_defeat_ip = %s where vhfmonthly_id = %s",[sdi,id])
       cursor.execute("update vhfmonthly set Squelch_op_phantom = %s where vhfmonthly_id = %s",[sop,id])
       cursor.execute("update vhfmonthly set Squelch_op_facilities = %s where vhfmonthly_id = %s",[sof,id])
       cursor.execute("update vhfmonthly set Squelch_op_marc = %s where vhfmonthly_id = %s",[som,id])
       cursor.execute("update vhfmonthly set Ready_signal = %s where vhfmonthly_id = %s",[rs,id])
       cursor.execute("update vhfmonthly set AGC = %s where vhfmonthly_id = %s",[agc,id])
       cursor.execute("update vhfmonthly set RF_pre_ATTN = %s where vhfmonthly_id = %s",[rpattn,id])
       cursor.execute("update vhfmonthly set squelch_carrier_override = %s where vhfmonthly_id = %s",[sco,id])
       cursor.execute("update vhfmonthly set squelch_threshold = %s where vhfmonthly_id = %s",[sqt,id])
       cursor.execute("update vhfmonthly set modulation_mode = %s where vhfmonthly_id = %s",[mm,id])
       cursor.execute("update vhfmonthly set squelch_defeat = %s where vhfmonthly_id = %s",[sqd,id])
       cursor.execute("update vhfmonthly set line_op = %s where vhfmonthly_id = %s",[lop,id])
       cursor.execute("update vhfmonthly set Unit_incharge_approval = %s where vhfmonthly_id = %s",["YES",id])
       remarks = "Parameter/s fixed"
       value = "All parameters NORMAL"
       val = (emp_id,remarks,value,currdate,currtime)
       sql = "INSERT INTO vhfmlogs (emp_id,remarks,value,date,time) values (%s ,%s, %s , %s,%s)"
       cursor.execute(sql,val)
       f=2
    
    print(f)
    vhf_m = models.Vhfmonthly.objects.all()
    vhf_m = vhf_m.values('vhfmonthly_id','date','time','modulation_mode','line_op','squelch_defeat','squelch_threshold','squelch_carrier_override','rf_pre_attn','agc','ready_signal','squelch_op_marc','squelch_op_facilities','squelch_op_phantom','squelch_defeat_ip','bit_test','unit_incharge_approval')
    vhf_m = vhf_m.filter(emp_id=id)
    return render(request,'engineer/vhf/vhfmonrep.html',{'vhf_m':vhf_m,'id':emp_id,'flag':f}) 
   

 