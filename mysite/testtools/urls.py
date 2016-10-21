from django.conf.urls import url
from . import views

app_name = 'testtools'
urlpatterns = [
    #url(r'^intf/$', views.IntfIndexView.as_view(), name='intfindex'),
    url(r'^intf/$',views.IntfIndex,name = 'intfindex'),

    url(r'^index/$',views.Index,name='index'),
    url(r'^index/(?P<category_id>[0-9]+)/$', views.IntfList, name='intflist'),
    url(r'^intf/datadesc/$', views.DataDesc, name='datadesc'),
]
