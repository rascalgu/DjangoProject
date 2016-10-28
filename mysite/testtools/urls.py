from django.conf.urls import url
from . import views

app_name = 'testtools'
urlpatterns = [
    url(r'^index/$',views.Index,name='index'),
    url(r'^index/(?P<category_id>[0-9]+)/$', views.IntfList, name='intflist'),

    url(r'^intf/datadesc/$', views.DataDesc, name='datadesc'),

    url(r'^intf/autodoc/$', views.AutoDoc, name='autodoc'),
    url(r'^intf/autodoc/topdf/$', views.ToPdf, name='topdf'),
]
