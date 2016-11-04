from django.conf.urls import url
from . import views

app_name = 'testtools'
urlpatterns = [
    url(r'^index/$',views.Interface_Test_Index,name='interface_test_index'),
    url(r'^index/(?P<category_id>[0-9]+)/$', views.Interface_Test_List, name='interface_test_list'),

    url(r'^intf/datadesc/$', views.DataDesc, name='datadesc'),

    url(r'^intf/autodoc/$', views.AutoDoc, name='autodoc'),
    url(r'^intf/autodoc/topdf/$', views.ToPdf, name='topdf'),
]
