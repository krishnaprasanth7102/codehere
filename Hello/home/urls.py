from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.bot, name= 'bot'),
    path('index', views.index, name = 'index'),
    path('mos/',views.mos, name='mos')
    
]

