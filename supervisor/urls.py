from django.contrib import admin
from django.urls import path,include
from . import views
from engineer import views as eviews
app_name='supervisor'
urlpatterns = [
    
    path('',views.main.choice,name='choice'),
    path('<int:id>/<str:name>', views.main.details),
    path('sendmail/<int:id>/',views.main.mail,name='sendmail'),
    path('sent/',views.main.sent,name='sent'),
    path('cdvordaily/',views.cdvor.daily,name='cdvordaily'),
    path('datisdaily/',views.datis.daily,name='datisdaily'),
    path('dmedaily/',views.dme.daily,name='dmedaily'),
    path('dscndaily/',views.dscn.daily,name='dscndaily'),
    path('ndb/',views.ndb.daily,name='ndbdaily'),
    path('scctvdaily/',views.scctv.daily,name='scctvdaily'),
    path('cdvorweekly/',views.cdvor.weekly,name='cdvorweekly'),
    path('datisweekly/',views.datis.weekly,name='datisweekly'),
    path('dmeweekly/',views.dme.weekly,name='dmeweekly'),
    path('dscnweekly/',views.dscn.weekly,name='dscnweekly'),
    path('scctvweekly/',views.scctv.weekly,name='scctvweekly'),
    path('ndb/',views.ndb.weekly,name='ndbweekly'),
    path('vhfweekly/',views.vhf.weekly,name='vhfweekly'),
    path('vhfdaily/',views.vhf.daily,name='vhfdaily'),
    path('scctvdaily/',views.scctv.daily,name='scctvdaily'),
    path('cdvormonthly/',views.cdvor.monthly,name='cdvormonthly'),
    # path('datismonthly/',views.datis.monthly,name='datismonthly'),
    path('dmemonthly/',views.dme.monthly,name='dmemonthly'),
    path('dscnmonthly/',views.dscn.monthly,name='dscnmonthly'),
    path('ndb/',views.ndb.monthly,name='ndbmonthly'),
    path('vhfmonthly/',views.vhf.monthly,name='vhfmonthly'),
    path('scctvmonthly/',views.scctv.monthly,name='scctvmonthly'),
    path('verify/<str:names>/<int:id>',views.main.verify,name='verify'),
    path('employee/<int:id>',views.main.empdetails)
   
    # path('employee/',views.employee)
    # path('officer/',views.officer)
    # path('install/', views.install),
    #  path('dummy/', views.dummy),
    #  path('test/', views.test)
]