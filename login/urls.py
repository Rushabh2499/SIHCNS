from django.contrib import admin
from django.urls import path,include
from . import views
from engineer import views as eviews
from django.contrib import admin
from django.urls import path,include
from . import views
from engineer.views.datis import viewsd as datviewsd
from engineer.views.datis import viewsw as datviewsw
from engineer.views.vhf import viewsd as vhfviewsd
from engineer.views.vhf import viewsm as vhfviewsm
from engineer.views.vhf import viewsy as vhfviewsy
from engineer.views.dscn import viewsd as dscnviewsd
from engineer.views.dscn import viewsm as dscnviewsm
from engineer.views.dscn import viewsw as dscnviewsw


urlpatterns = [
    path('',views.login),
    path('validate/',views.validate),
    # path('engineer/',eviews.test),
    path('schoice/',include('supervisor.urls')),
    path('',views.login),
    path('validate/',views.validate),
    path('dhomeview/',views.dhomeview),
    path('dhomeviews/<int:id>',views.dhomeview),
    path('dgmhome/', views.pie_chart, name='dgmhome'),

    

    #vhf 
    #daily
    path('vhfdaily/<int:id>',vhfviewsd.vhfd),
    path('vhfdailyrep/<int:id>',vhfviewsd.vhfdrep),
    path('vhfrepsub/<int:id>',vhfviewsd.vhfdrepsub), 
    path('vhfdailylogs/<int:id>',vhfviewsd.vhfdlogs), 
    path('editvhfd/<int:vhfdaily_id>',vhfviewsd.editvhfdaily), 
    path('upvhfrepsub/<int:id>',vhfviewsd.upvhfdaily),
    path('routebackvd/<int:id>/',vhfviewsd.routebackvhfd),    
    path('vhfdailyrec/<int:id>/',vhfviewsd.vhfdailyrec),    
    
    #monthly
    path('vhfmonthly/<int:id>',vhfviewsm.vhfm),
    path('vhfmonthlyrep/<int:id>',vhfviewsm.vhfmrep),
    path('vhfmrepsub/<int:id>',vhfviewsm.vhfmrepsub),
    path('vhfmlogs/<int:id>',vhfviewsm.vhfmlogs),
    path('editvhfm/<int:vhfmonthly_id>',vhfviewsm.editvhfmonthly),
    path('upvhfmrepsub/<int:id>',vhfviewsm.upvhfmonthly),
    
    #yearly
    path('vhfyearly/<int:id>',vhfviewsy.vhfy),
    path('vhfyearlyrep/<int:id>',vhfviewsy.vhfyrep),
    path('vhfyrepsub/<int:id>',vhfviewsy.vhfyrepsub),
    path('vhfylogs/<int:id>',vhfviewsy.vhfylogs),
    path('editvhfy/<int:vhfyearly_id>',vhfviewsy.editvhfyearly),
    path('upvhfyrepsub/<int:id>',vhfviewsy.upvhfyearly),
  
    #dscn #daily
    path('dscndaily/<int:id>',dscnviewsd.dscnd),
    path('dscndailyrep/<int:id>',dscnviewsd.dscndrep),
    path('dscnrepsub/<int:id>',dscnviewsd.dscndrepsub),
    path('routebackdsd/<int:id>',dscnviewsd.routebackdscnd),
    path('editdscnd/<int:dscndaily_id>',dscnviewsd.editdscndaily),
    path('updscnrepsub/<int:id>',dscnviewsd.updscndaily),
    path('dscndailylogs/<int:id>',dscnviewsd.dscndailylogs),
   
    #weekly
    path('dscnweekly/<int:id>',dscnviewsw.dscnw),
    path('dscnweeklyrep/<int:id>',dscnviewsw.dscnwrep),
    path('dscnwrepsub/<int:id>',dscnviewsw.dscnwrepsub),
    path('editdscnw/<int:dscnweekly_id>',dscnviewsw.editdscnweekly),
    path('updscnwrepsub/<int:id>',dscnviewsw.updscnweekly),
    path('dscnweeklylogs/<int:id>',dscnviewsw.dscnweeklylogs),
    
    #monthly
    path('dscnmonthly/<int:id>',dscnviewsm.dscnm),
    path('dscnmonthlyrep/<int:id>',dscnviewsm.dscnmrep),
    path('dscnmrepsub/<int:id>',dscnviewsm.dscnmrepsub),
    path('dscnmonthlylogs/<int:id>',dscnviewsm.dscnmonthlylogs),
    path('editdscnm/<int:dscnmonthly_id>',dscnviewsm.editdscnmonthly),
    path('updscnmrepsub/<int:id>',dscnviewsm.updscnmonthly),
   
    #datis
   #daily 
    path('datisdaily/<int:id>',datviewsd.datisd),
    path('datisdailyrep/<int:id>',datviewsd.datisdrep),
    path('datisrepsub/<int:id>',datviewsd.datisdrepsubm),
    path('editdatisd/<int:p_id>',datviewsd.editdatisdaily),
    path('updatisrepsub/<int:id>',datviewsd.updatisdaily),
    path('routebackdd/<int:id>/',datviewsd.routebackdatisd),
    path('logout/<int:id>',datviewsd.logoutd),
    path('datisdailyrec/<int:id>',datviewsd.datisdailyrec),
    path('repsuberrors/<int:p_id>/<int:id>',datviewsd.repsuberrors),
    path('finalrepsub/<int:p_id>/<int:id>',datviewsd.finalrepsub),
    #path('email/',datviewsd.email),
    path('sent/',datviewsd.sent),
    #added new route
    path('homed/<int:id>/<int:p_id>',datviewsd.homed),
    
    #weekly
    path('datisweekly/<int:id>',datviewsw.datisw),
    path('datisweeklyrep/<int:id>',datviewsw.datiswrep),
    path('datisweeklyrec/<int:id>',datviewsw.datisweeklyrec),
    path('datiswrepsub/<int:id>',datviewsw.datiswrepsubw),
    path('editdatisw/<int:p_id>',datviewsw.editdatisweekly),
    path('updatiswrepsub/<int:id>',datviewsw.updatisweekly),
    path('repsubwerrors/<int:p_id>/<int:id>',datviewsw.repsubwerrors),
    path('finalwrepsub/<int:p_id>/<int:id>',datviewsw.finalwrepsub),
    path('homew/<int:id>/<int:p_id>',datviewsw.homew)
   
    # path('engineer/',include('supervisor.urls'))
    # path('employee/',views.employee)
    # path('officer/',views.officer)
    # path('install/', views.install),
    #  path('dummy/', views.dummy),
    #  path('test/', views.test)
]
