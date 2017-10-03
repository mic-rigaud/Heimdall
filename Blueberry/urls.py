"""Blueberry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from Main_UI import views as Main_UI
from Network_Analyst import views as Network_Analyst

urlpatterns = [
    url(r'^$', Main_UI.home, name='home'),
    url(r'^settings/$', Main_UI.settings, name='settings'),
    url(r'^task/$', Network_Analyst.tasks, name='task'),
    url(r'^about/$', Main_UI.about, name='about'),
    url(r'^delete/(?P<ip_d>.+)/(?P<mac_d>.+)$', Main_UI.delete_entry, name='delete')
    # url(r'^network_analyst/', include('Network_Analyst.urls')),
]
