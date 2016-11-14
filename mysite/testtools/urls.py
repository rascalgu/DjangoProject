from django.conf.urls import url
from . import views

app_name = 'testtools'
urlpatterns = [

    url(r'^index/$',views.Index,name='index'),
    url(r'^addproject/$',views.AddProject,name='addproject'),

    url(r'^project/list$',views.Project_List,name='project_list'),
    url(r'^project/(?P<project_id>[0-9]+)/$', views.Project_List_ById, name='project_list_byid'),
    url(r'^project/list/ajax/(?P<project_id>[0-9]+)/$', views.Ajax_Interface_List, name='ajax_interface_list'),


    url(r'^interface/detail/(?P<interface_id>[0-9]+)/$', views.Interface_Test_Detail, name='interface_test_detail'),
    #url(r'^interface/list/ajax/(?P<category_id>[0-9]+)/$', views.Ajax_Interface_List, name='ajax_interface_list'),

    url(r'^datadesc/$', views.DataDesc, name='datadesc'),

    url(r'^intf/autodoc/$', views.AutoDoc, name='autodoc'),
    url(r'^intf/autodoc/topdf/$', views.ToPdf, name='topdf'),
]
