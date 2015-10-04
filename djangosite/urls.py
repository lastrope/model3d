"""djangosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, handler404
from django.contrib import admin

from users import urls as u_urls
from home import urls as h_urls
from model3d import urls as m_urls
from badges import urls as b_urls

urlpatterns = [
    url(r'^', include(h_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include(u_urls)),
    url(r'^models/', include(m_urls)),
    url(r'^badges/', include(b_urls)),
]

handler404 = 'request_handler.views.handler404'