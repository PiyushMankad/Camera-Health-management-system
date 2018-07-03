#!python
# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'report/$', views.report, name='report'),
    url(r'chart/$', views.chart, name='chart'),
    url(r'weekly/$', views.weekly, name='weekly'),
    url(r'monthly/$', views.monthly, name='monthly'),
    url(r'custom/$', views.custom, name='custom'),
]

