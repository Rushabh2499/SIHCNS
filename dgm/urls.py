from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from . import views



app_name='dgm'
urlpatterns = [
    # path('communication/',views.communication,name='communication'),
    # path('',views.main.choice,name='choice'),
    path('navigation/', views.navigation,name='navigation'),
    # path('surveillance/', views.navigation,name='sur')
    path('<str:id>/<str:name>', views.details,name='details'),
    path('communication/',views.communication),
	



]