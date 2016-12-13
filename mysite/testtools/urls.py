from django.conf.urls import url
from . import views

app_name = 'testtools'
urlpatterns = [

    url(r'^index/$',views.Index,name='index'),

    #---------------------forms------------------------------------
    url(r'^project/addproject/$',views.AddProject,name='addproject'),
    url(r'^project/addmessage/$',views.AddMessage,name='addmessage'),
    #--------------------------------------------------------------

    #---------------------ajax--------------------------------------
    url(r'^project/list/ajax/(?P<project_id>[0-9]+)/$', views.Ajax_Scenario_List, name='ajax_scenario_list'),
    #----------------------------------------------------------------

    #---------------------project------------------------------------
    url(r'^project/list/$',views.project_list,name='project_list'),
    url(r'^project/detail/scenario/(?P<project_id>[0-9]+)/$',views.project_detail_scenario,name='project_detail_scenario'),
    url(r'^project/detail/interface/(?P<project_id>[0-9]+)/$',views.project_detail_interface,name='project_detail_interface'),
    url(r'^project/(?P<project_id>[0-9]+)/$', views.Project_List_ById, name='project_list_byid'),
    #----------------------------------------------------------------

    #---------------------scenario------------------------------------
    url(r'^scenario/list/$',views.scenario_list,name='scenario_list'),
    url(r'^scenario/detail/(?P<scenario_id>[0-9]+)/$',views.scenario_detail,name='scenario_detail'),
    url(r'^scenario/statetest/ajax/(?P<scenario_id>[0-9]+)/$',views.ajax_scenario_statetest,name='ajax_scenario_statetest'),
    url(r'^scenario/resetstate/ajax/(?P<scenario_id>[0-9]+)/$',views.ajax_scenario_resetstate,name='ajax_scenario_resetstate'),
    #-----------------------------------------------------------------


    #---------------------interface------------------------------------
    url(r'^interface/list/$',views.interface_list,name='interface_list'),
    #url(r'^interface/detail/(?P<interface_id>[0-9]+)/$',views.interface_detail,name='interface_detail'),
    url(r'^interface/detail/(?P<interface_id>[0-9]+)/$', views.Interface_Test_Detail, name='interface_test_detail'),
    #------------------------------------------------------------------


    url(r'^intf/autodoc/$', views.AutoDoc, name='autodoc'),
    url(r'^intf/autodoc/topdf/$', views.ToPdf, name='topdf'),
]
