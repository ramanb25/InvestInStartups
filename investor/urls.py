"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    # url(r'form/$',views.forms,name='forms'),
    # url(r'disp/$',views.disp,name='disp'),
    # url(r'debit/$',views.debit,name='debit'),
    # url(r'buy/$',views.redirectBuy,name='buy'),
    # url(r'sell/$',views.redirectSell,name='sell'),
    # url(r'execBuy/$',views.execBuy,name='execBuy'),
    # url(r'^register/$', views.register, name='register'),
    # url(r'^login/$', views.user_login, name='login'),
    # url(r'^logout/$', views.user_logout, name='logout'),
    # url(r'^restricted/', views.restricted, name='restricted'),
    # url(r'^profile/$', views.profile, name='profile'),

    
]
