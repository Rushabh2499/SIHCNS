from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from login.models import Engineer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from datetime import date,datetime,timedelta
from django.db import connection

# Create your views here.

from django.http import HttpResponse
from . import models
from django.db import connection
# Create your views here.
def login(request):
     if request.session.has_key('uid'):
         id = request.session['uid']
         uid = id
         s0 = models.Engineer.objects.all()
         s0 = s0.values('a_id')
         s0 = s0.filter(emp_id=id)
         cursor = connection.cursor() 

         _q = models.Airport.objects
         _q = _q.filter(a_id__in=s0)
         name1 = _q.all()
                    
         q = models.Engineer.objects
                    
         q = q.values('name','designation','a_id')
         q = q.filter(emp_id=id)
                    
         empdetails = q.all()
         supdetails = models.Supervisor.objects.all()
         supdetails = supdetails.values('name','contact','email').filter(dept='C')
         statusd = "" 
        #!!!!!!!!!!!!!!!!!datis daily!!!!!!!!!!!!!!!!!!!!!!!!
         ddr = 0
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
            if (datisd_deadline <= date.today()) :    
                #remarks = "---Report not submitted---"
                #statusd = "COMPLETED"
                #val = ((date.today()-timedelta(days=1)),id,status,'2',remarks)
                #sql = "INSERT INTO datisdaily (date,emp_id,status,f_id,remarks) values (%s ,%s,%s, %s,%s)"
                #cursor.execute(sql,val)  
                datisdsub_on = date.today()-timedelta(days=1)    
            else : 
                datisd_deadline = date.today()
         print(ddr)
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
         wdate = wdate + timedelta(days=7) 
         dwr = 0
         datiswsub_on = temp
         datiswsub_deadline =  wdate 
         status = ""
         if currdate > wdate :  #if it goes beyond 7 days
            #remarks = "Report not submitted"
            #value = "No Entry" 
            #val = (id,p_id,remarks,value,currdate,currtime)
            #sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s ,%s, %s,%s)"
            #cursor.execute(sql,val)
            dwr = 0

         elif currdate == temp : # report submitted today
            status = models.Datisweekly.objects.all()
            status = status.values('date','status')
            status = status.order_by('-date')
            status = status.values('status')
            status = status.values('status').filter(a_id=1)[0]['status']
            if status == "COMPLETED" :
                dwr=1  
            elif status == "PENDING" :
                dwr=0
                datiswsub_deadline = wdate1 + timedelta(days=7)   
            elif status == "COMPLETED WITH ERRORS" :  
                dwr = 1    
    
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!vhfdaily!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
         statusvd = ""
         vdr = 0
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
                val = ((date.today()-timedelta(days=1)),id,status,'1',remarks)
                sql = "INSERT INTO vhfdaily (date,emp_id,status,f_id,remarks) values (%s ,%s,%s, %s,%s)"
                cursor.execute(sql,val)  
                vhfdsub_on = date.today()-timedelta(days=1)    
            else : 
                vhfd_deadline = date.today()
         '''
    #     #!!!!!!!!!!!!!!!!!!!!!!!vhfmonthly!!!!!!!!!!!!!!!!!!!!!!!!!!!!        
    #     vmr = 0
    #     currdate = date.today()
    #     wdate = models.Vhfmonthly.objects.all()
    #     wdate = wdate.values('date')
    #     wdate = wdate.order_by('-date')
    #     wdate = wdate.values('date').filter(a_id=1)[0]['date']
    #     wdate = str(wdate)
    #     wdate = datetime.strptime(wdate, "%Y-%m-%d").date()
    #     temp = wdate
    #     wdate = wdate + timedelta(days=30) 
    #     #vhfmsub_on = cursor.execute("select date from vhfmonthly where date = %s",[temp])    
    #     vhfmsub_on = temp
    #     if currdate > wdate :
    #         vhfmsub_deadline =  currdate 
    #     else :
    #         vhfmsub_deadline =  wdate
    #         vmr = 1
    #     #!!!!!!!!!!!!!!!!!!!!!!!!vhfyearly!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #     vyr = 0
    #     currdate = date.today()
    #     wdate = models.Vhfyearly.objects.all()
    #     wdate = wdate.values('date')
    #     wdate = wdate.order_by('-date')
    #     wdate = wdate.values('date').filter(a_id=1)[0]['date']
    #     wdate = str(wdate)
    #     wdate = datetime.strptime(wdate, "%Y-%m-%d").date()
    #     temp = wdate
    #     wdate = wdate + timedelta(days=365) 
    #     #vhfysub_on = cursor.execute("select date from vhfyearly where date = %s",[temp])    
    #     vhfysub_on = temp
    #     if currdate > wdate :
    #         vhfysub_deadline =  currdate 
    #     else :
    #         vhfysub_deadline =  wdate
    #         vyr = 1

    #     #!!!!!!!!!!!!!!!!!!!!!!!!!!dscndaily!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
    #     dsdr = 0
    #     currdate = date.today()            
    #     dscndsub_on = cursor.execute("select date from dscndaily where date = %s",[date.today()])    
    #     if dscndsub_on :
    #         dscnd_deadline = currdate + timedelta(days=1)
    #         dscndsub_on = currdate
    #         dsdr =1 
            
    #     else :
    #         dscnd_deadline = models.Dscndaily.objects.all()
    #         dscnd_deadline = dscnd_deadline.values('date')
    #         dscnd_deadline = dscnd_deadline.order_by('-date')
    #         dscnd_deadline = dscnd_deadline.values('date').filter(a_id=1)[0]['date']
    #         dscndsub_on = dscnd_deadline
    #         dscnd_deadline = dscnd_deadline + timedelta(days=2)
    #         if (dscnd_deadline <= date.today()) :    
    #             remarks = "---Report not submitted---"
    #             val = ((date.today()-timedelta(days=1)),id,'2',remarks)
    #             sql = "INSERT INTO dscndaily (date,emp_id,f_id,remarks) values (%s ,%s, %s,%s)"
    #             cursor.execute(sql,val)  
    #             dscndsub_on = date.today()-timedelta(days=1)    
    #         else : 
    #             dscnd_deadline = date.today()

    #     #!!!!!!!!!!!!!!!!!!!!!!!!dscnweekly!!!!!!!!!!!!!!!!!!!!!!!!!!
    #     currdate = date.today()
    #     wdate = models.Dscnweekly.objects.all()
    #     wdate = wdate.values('date')
    #     wdate = wdate.order_by('-date')
    #     wdate = wdate.values('date').filter(a_id=1)[0]['date']
    #     wdate = str(wdate)
    #     wdate = datetime.strptime(wdate, "%Y-%m-%d").date()
    #     temp = wdate
    #     wdate = wdate + timedelta(days=7) 
    #     dswr = 0
    #     dscnwsub_on = temp
    #     if currdate > wdate :
    #         dscnwsub_deadline =  currdate 
    #     else :
    #         dscnwsub_deadline =  wdate
    #         dswr =1 

    #     #!!!!!!!!!!!!!!!!!!!!!!!!dscnmonthly!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #     dsmr = 0
    #     currdate = date.today()
    #     wdate = models.Dscnmonthly.objects.all()
    #     wdate = wdate.values('date')
    #     wdate = wdate.order_by('-date')
    #     wdate = wdate.values('date').filter(a_id=1)[0]['date']
    #     wdate = str(wdate)
    #     wdate = datetime.strptime(wdate, "%Y-%m-%d").date()
    #     temp = wdate
    #     wdate = wdate + timedelta(days=30) 
    #     dscnmsub_on = temp
    #     if currdate > wdate :
    #         dscnmsub_deadline =  currdate 
    #     else :
    #         dscnmsub_deadline =  wdate
    #         dsmr = 1

    #     return render(request,'./engineer/home.html',{'status':status,'dscnmsub_deadline':dscnmsub_deadline,'dscnmsub_on':dscnmsub_on,'dsmr':dsmr,'dswr':dswr,'dscnwsub_on':dscnwsub_on,'dscnwsub_deadline':dscnwsub_deadline,'dscnd_deadline':dscnd_deadline,'dscndsub_on':dscndsub_on,'dsdr':dsdr,'ddr':ddr,'dwr':dwr,'vdr':vdr,'vmr':vmr,'vyr':vyr,'currdate':currdate,'name':name1,'id':id,'empdet':empdetails,'datisdsub_on':datisdsub_on,'datisd_deadline':datisd_deadline,'datiswsub_on':datiswsub_on,'datiswsub_deadline':datiswsub_deadline,'vhfdsub_on':vhfdsub_on,'vhfd_deadline':vhfd_deadline,'vhfmsub_on':vhfmsub_on,'vhfmsub_deadline':vhfmsub_deadline,'vhfysub_on':vhfysub_on,'vhfysub_deadline':vhfysub_deadline})'''
         return render(request,'./engineer/home.html',{'vhfdsub_on':vhfdsub_on,'vhfd_deadline':vhfd_deadline,'wdate':wdate,'supdetails':supdetails,'statusvd':statusvd,'statusd':statusd,'status':status,'ddr':ddr,'dwr':dwr,'currdate':currdate,'name':name1,'id':id,'empdet':empdetails,'datisdsub_on':datisdsub_on,'datisd_deadline':datisd_deadline,'datiswsub_on':datiswsub_on,'datiswsub_deadline':datiswsub_deadline,'vdr':vdr,})
     else:
         return render(request,'login/login.html')
# uid=''
# passw=''
    # p=Engineer(emp_id=4133,name='bobby',designation='JET',a_id=1,dept='N',contact='44499',password='amdvh',supervisor_id=3112)
    # p.save()
    # x=models.Dgm.objects.all()
    # for i in x:
    #         user = User.objects.create_user(username=i.dgm_id,password=i.password)
    #         user.save()
    # x=models.Supervisor.objects.all()
    # for i in x:
    #         user = User.objects.create_user(username=i.supervisor_id,password=i.password)
    #         user.save()
    # x=models.Engineer.objects.all()
    # for i in x:
    #         user = User.objects.create_user(username=i.emp_id,password=i.password)
    #         user.save()    
    # x=models.Head.objects.all()
    # for i in x:
    #         user = User.objects.create_user(username=i.head_id,password=i.password)
    #         user.save()

            # 
        # uid=''
        # passw=''
        #request.session['type']='start'
     #   return render(request,'login/login.html')

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
        flag = 0
        x=models.Engineer.objects.all()
        for i in x:               
            if (uid == str(i.emp_id)) & (check_password(passw,i.password)) :
               #    request.session['type']='e'
                return dhomeview(request,id) 
    elif b=='21' :
        x=models.Dgm.objects.all()
        for i in x:
            if (uid == str(i.dgm_id)) & (passw == i.password) :
                flag=0
                y=models.Airport.objects.filter(a_id=i.a_id).values()
                print(y[0])
                return render(request,'./dgm/dgm.html',{'name':y[0]})
    elif b=='11' :
        x=models.Head.objects.all()
        for i in x:
            if (uid == str(i.head_id)) & (check_password(passw,i.password)):
                flag=0
                # y=models.Airport.objects.filter(a_id=i.a_id).values()
                # print(y[0])

                return render(request,'./head/head.html')
    elif b=='31' :
                   
        x=models.Supervisor.objects.all()
        # print(models.Datisdaily.objects.all().values())
        # context={
        # 'cdvordaily':[entry for entry in models.Cdvordaily.objects.all().values()],
        # 'datisdaily':[entry1 for entry1 in models.Datisdaily.objects.all().values()],
        # 'dmedaily':[entry for entry in models.Dmedaily.objects.all().values()],
        # 'dscndaily':[entry for entry in models.Dscndaily.objects.all().values()],
        # 'ndbdaily':[entry for entry in models.Ndbdaily.objects.all().values()],
        # 'scctvdaily':[entry for entry in models.Scctvdaily.objects.all().values()],
        # 'vhfdaily':[entry for entry in models.Vhfdaily.objects.all().values()]
        # }
        # list_result=[{}]
        # for k,v in context.items():
        #     list_result=[entry for entry in context[k]]
        # print(list_result)
        # for i in list_result:
        #     for k,v in i:
        #         print(v)
        for i in x:
            print(check_password(passw,i.password))
            if (uid == str(i.supervisor_id)) & (check_password(passw,i.password)) :
                flag=0
                # y=models.Airport.objects.filter(a_id=i.a_id).values()
                # print(y[0])
                request.session['type']='s'
                request.session['uid']=uid
                request.session['passw']=passw
                # print(request.session['uid'])
                supInfo=models.Supervisor.objects.filter(supervisor_id=uid).values()
                airInfo=models.Airport.objects.filter(a_id=supInfo[0]['a_id']).values('name')
                print(airInfo)
                dgm=models.Dgm.objects.filter(a_id=supInfo[0]['a_id']).values()
                datisdaily=[entry for entry in models.Datisdaily.objects.filter(status='PENDING').values()]
                id=uid
                datisweekly=[entry for entry in models.Datisweekly.objects.filter(status='PENDING').values()]
                datis=datisdaily+[i for i in datisweekly]
                for i in datis:
                    i.update({'type':'Datisdaily'})
                # print(datisdaily)
                eng=models.Engineer.objects.all().values()
                context=dhomeview_sup()
                print(context)
                
                context.update({'sup':supInfo[0],'dgm':dgm[0],'datis':datis,'eng':eng,'air':airInfo[0]})
                print(context['datisd_deadline'])
                return render(request,'./supervisor/home.html',context)
                



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
            return render(request,'login/login.html',{'flag':flag})
def dhomeview_sup() :
  
    cursor = connection.cursor() 
    # s0 = models.Engineer.objects.all()
    # s0 = s0.values('a_id')
    # s0 = s0.filter(emp_id=id)

    # _q = models.Airport.objects
    # _q = _q.filter(a_id__in=s0)
    # name1 = _q.all()
                
    # q = models.Engineer.objects
    # q = q.values('name','designation','a_id')
    # q = q.filter(emp_id=id)
    # empdetails = q.all()
    ddr =0           

    status = "" 
        #!!!!!!!!!!!!!!!!!datis daily!!!!!!!!!!!!!!!!!!!!!!!!
    currdate = date.today()
    currtime = datetime.now().strftime("%H:%M:%S")            
    datisdsub_on = cursor.execute("select date from datisdaily where date = %s",[date.today()])    
    if datisdsub_on :
        status = models.Datisdaily.objects.all()
        status = status.values('date','status')
        status = status.order_by('-date')
        status = status.values('status')
        status = status.values('status').filter(a_id=1)[0]['status']
        if status == "PENDING" :
            datisdsub_on = currdate
            datisd_deadline = currdate
            ddr=0
        else :
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
            # remarks = "---Report not submitted---"
            # status = "COMPLETED"
            # val = ((date.today()-timedelta(days=1)),id,status,'2',remarks)
            # sql = "INSERT INTO datisdaily (date,emp_id,status,f_id,remarks) values (%s ,%s,%s, %s,%s)"
            # cursor.execute(sql,val)  
            datisdsub_on = date.today()-timedelta(days=1)    
        else : 
            datisd_deadline = date.today()
    # print("here")
    datisd_deadline1=datisd_deadline.strftime('%d/%m/%Y')
    datisdsub_on1=datisdsub_on.strftime('%d/%m/%Y')
    context={'ddr':ddr,'currdate':currdate,'datisdsub_on':datisdsub_on1,'datisd_deadline':datisd_deadline1}
    return context

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
        if (datisd_deadline <= date.today()) :    
            remarks = "---Report not submitted---"
            statusd = "COMPLETED"
            val = ((date.today()-timedelta(days=1)),id,statusd,'2',remarks)
            sql = "INSERT INTO datisdaily (date,emp_id,status,f_id,remarks) values (%s ,%s,%s, %s,%s)"
            cursor.execute(sql,val)  
            datisdsub_on = date.today()-timedelta(days=1)    
        else : 
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
    wdate = wdate + timedelta(days=7) 
    dwr = 0
    datiswsub_on = temp
    datiswsub_deadline =  wdate 
    status = ""
    if currdate > wdate :  #if it goes beyond 7 days
        remarks = "Report not submitted"
        value = "No Entry" 
        val = (id,p_id,remarks,value,currdate,currtime)
        sql = "INSERT INTO datiswlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s ,%s, %s,%s)"
        cursor.execute(sql,val)
        dwr = 0
        
    elif currdate == temp : # report submitted today
        status = models.Datisweekly.objects.all()
        status = status.values('date','status')
        status = status.order_by('-date')
        status = status.values('status')
        status = status.values('status').filter(a_id=1)[0]['status']
        if status == "COMPLETED" :
            dwr=1  
        elif status == "PENDING" :
            dwr=0
            datiswsub_deadline = wdate1 + timedelta(days=7)   
    
    print(dwr)
    
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
    
    '''
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
    '''
    #return render(request,'./engineer/home.html',{'status':status,'dscnmsub_deadline':dscnmsub_deadline,'dscnmsub_on':dscnmsub_on,'dsmr':dsmr,'dswr':dswr,'dscnwsub_on':dscnwsub_on,'dscnwsub_deadline':dscnwsub_deadline,'dscnd_deadline':dscnd_deadline,'dscndsub_on':dscndsub_on,'dsdr':dsdr,'ddr':ddr,'dwr':dwr,'vdr':vdr,'vmr':vmr,'vyr':vyr,'currdate':currdate,'name':name1,'id':id,'empdet':empdetails,'datisdsub_on':datisdsub_on,'datisd_deadline':datisd_deadline,'datiswsub_on':datiswsub_on,'datiswsub_deadline':datiswsub_deadline,'vhfdsub_on':vhfdsub_on,'vhfd_deadline':vhfd_deadline,'vhfmsub_on':vhfmsub_on,'vhfmsub_deadline':vhfmsub_deadline,'vhfysub_on':vhfysub_on,'vhfysub_deadline':vhfysub_deadline})
    return render(request,'./engineer/home.html',{'vhfdsub_on':vhfdsub_on,'vhfd_deadline':vhfd_deadline,'wdate':wdate,'supdetails':supdetails,'statusvd':statusvd,'statusd':statusd,'status':status,'ddr':ddr,'dwr':dwr,'currdate':currdate,'name':name1,'id':id,'empdet':empdetails,'datisdsub_on':datisdsub_on,'datisd_deadline':datisd_deadline,'datiswsub_on':datiswsub_on,'datiswsub_deadline':datiswsub_deadline,'vdr':vdr,})
 

def std(request,id) :
     if request.session.has_key('uid'):
        return render(request,'login/standards.html')  
     else :
        return render(request,'login/login.html')     