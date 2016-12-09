# -*- coding: utf-8 -*-
from .models import Project,Category,Interface,RequestParam,ResponseParam,TestScenarios
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.http import HttpResponse
from .forms import ProjectForm
from reportlab.pdfgen import canvas
from cStringIO import StringIO
from reportlab import  rl_config
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch
from reportlab.lib.utils import simpleSplit
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.fonts import addMapping
from django.http import HttpResponse
from django.core import serializers

import os

def findProjectListAll():
    project_list = Project.objects.all()
    return project_list

def findInterfaceListByProjectId(project_id):
    interface_list = serializers.serialize("json",Interface.objects.filter(project_id = project_id))
    return interface_list

def Ajax_Scenario_List(request,project_id):
    scenario_list = serializers.serialize("json",TestScenarios.objects.filter(project_id = project_id))
    return HttpResponse(scenario_list)


def findCategoryByAll():
    category_list = Category.objects.all()
    return category_list

def findInterfaceByAll():
    interface_list = Interface.objects.all()
    return interface_list

def findInterfaceListById(category_id):
    interface_list = serializers.serialize("json",Interface.objects.filter(category_id = category_id))
    return interface_list

def findInterfaceDetailById(interface_id):
    interface_detail = Interface.objects.filter(id = interface_id)
    return interface_detail


def Index(request):
    return  render(request,'testtools/index.html')

def project_list(request):
    project_list = Project.objects.all()
    return render(request, 'testtools/project_list.html',{'project_list':project_list})


def project_detail_scenario(request,project_id):
    project_list = findProjectListAll()
    project_name = Project.objects.get(id = project_id)
    scenario_list = TestScenarios.objects.filter(project_id = project_id)
    return render(request, 'testtools/project_detail_scenario.html',{'project_list':project_list,'project_name': project_name,'scenario_list':scenario_list,'project_id':project_id})

def project_detail_interface(request,project_id):
    project_list = findProjectListAll()
    project_name = Project.objects.get(id = project_id)
    interface_list = Interface.objects.filter(project_id = project_id)
    return render(request, 'testtools/project_detail_interface.html',{'project_list':project_list,'project_name': project_name,'interface_list':interface_list,'project_id':project_id})


def scenario_list(request):
    project_list = findProjectListAll()
    scenario_list = TestScenarios.objects.all()
    return render(request, 'testtools/scenario_list.html',{'project_list':project_list,'scenario_list':scenario_list})

def scenario_detail(request,scenario_id):
    project_list = findProjectListAll()
    scenario_list = TestScenarios.objects.filter(id = scenario_id)
    return render( request,'testtools/project_detail_scenario.html',{'project_list':project_list,'scenario_list':scenario_list})

def ajax_scenario_statetest(request,scenario_id):

    scenario = TestScenarios.objects.get(id = scenario_id)
    interface_list = scenario.interfaces.all()
    times = range(len(interface_list))

    threads = []

    for list in interface_list:
        scenario = TestScenarios.objects.get(id = scenario_id)
        scenario.state = '1'
        scenario.save()
        thread_request_link = list.request_link + '?'
        thread_request_param= RequestParam.objects.filter(interface_id = list.id)

        thread_param = {}
        for i in thread_request_param:
            thread_param[i.request_param_name] = i.request_param_value

        #print thread_request_link
        #print thread_param

        #调用ThreadFunc实例化的对象，创建所有线程
        t = StateTestThread(thread_request_link,thread_param)
        threads.append(t) #加入线程
        #print threads

    #开始线程
    for i in times:
        threads[i].start() #启动线程

    #等待所有结束线程
    for i in times:
        threads[i].join()

    interface_state = threads[i].get_result()
    if interface_state == 0:
        scenario = TestScenarios.objects.get(id = scenario_id)
        scenario.state = '2'
        scenario.save()
    else:
        scenario = TestScenarios.objects.get(id = scenario_id)
        scenario.state = '3'
        scenario.save()

    scenario_list = serializers.serialize("json",TestScenarios.objects.filter(id = scenario_id))
    return HttpResponse(scenario_list)


import threading,urllib2,urllib,json

class StateTestThread(threading.Thread):

    def __init__(self,url,param):
        threading.Thread.__init__(self)
        self.url = url
        self.param = param

    def run(self):
        post_data = urllib.urlencode(self.param)
        response = urllib2.urlopen(self.url, post_data)
        code = response.getcode()
        content = response.read()
        contentjson = json.loads(content)
        state = contentjson['return_code']
        if (code == 200) and (state == 0) :
            self.result = 0
        else:
            self.result = 1

    def get_result(self):
        return self.result

def ajax_scenario_resetstate(request,scenario_id):
    scenario = TestScenarios.objects.get(id = scenario_id)
    scenario.state = '0'
    scenario.save()
    scenario_list = serializers.serialize("json",TestScenarios.objects.filter(id = scenario_id))
    return HttpResponse(scenario_list)

def interface_list(request):
    project_list = findProjectListAll()
    interface_list = Interface.objects.all()
    return render(request, 'testtools/interface_list.html',{'project_list':project_list,'interface_list':interface_list})

def interface_detail(request,interface_id):
    interface_list = Interface.objects.filter(id = interface_id)
    return render(request,'testtools/interface_list.html',{'interface_list':interface_list})


def Interface_Test_Detail(request,interface_id):
    project_list = findProjectListAll()
    category_list = findCategoryByAll()
    interface_detail = Interface.objects.filter(id = interface_id)
    request_param = RequestParam.objects.filter(interface_id = interface_id)
    return render(request,'testtools/new_interface_detail.html',{'interface_detail':interface_detail,'category_list': category_list,'project_list':project_list,'request_param':request_param})


def Project_List_ById(request,project_id):
    project_list = findProjectListAll()
    scenario_list = findScenarioListByProjectId(project_id)
    interface_list = findInterfaceListByProjectId(project_id)
    return render(request,'testtools/project_list.html',{'project_list': project_list,'interface_list':interface_list,'scenario_list':scenario_list})

def AddProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            projectname = form.cleaned_data['project_name']
            project = Project()
            project.project_name = projectname
            project.save()
            return HttpResponseRedirect('/testtools/project/list')
    else:
        form = ProjectForm()
    return render(request,'testtools/project_list.html',{'form':form})



def AutoDoc(request):
    category_list = findCategoryByAll()
    interface_list = findInterfaceByAll()
    return render(request, 'testtools/autodoc.html',{'category_list':category_list,'interface_list':interface_list})

def ToPdf(request):

    rl_config.warnOnMissingFontGlyphs = 0
    path ="D:\\Program Files\\Python\\Lib\\site-packages\\reportlab\\fonts"
    pdfmetrics.registerFont(TTFont('hei',os.path.join(path, 'simhei.ttf')))

    addMapping('cjk',0,0,'hei')

    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="大数据交易中心接口文档.pdf"'

    temp = StringIO()
    p = canvas.Canvas(temp)


    interface_list=findInterfaceByAll()
    for interface in interface_list:
        p.setFont('hei',16)
        p.leading = 20
        p.drawString(50,800,interface.interface_sn)
        p.drawString(100,800,interface.interface_name)
        p.drawString(50,780,"请求方式:")
        p.drawString(125,780,interface.request_method)
        p.drawString(50,760,"请求url:")
        p.drawString(50,740,interface.request_link)

        p.drawString(50,630,"参数名")
        p.drawString(200,630,"参数类型")
        p.drawString(280,630,"必填")
        p.drawString(320,630,"说明")

        request_param_list = RequestParam.objects.filter(interface__id = interface.id)
        for i in range(len(request_param_list)):
            p.drawString(50,550+i*20,request_param_list[i].request_param_name)
            p.drawString(200,550+i*20,request_param_list[i].request_param_type)
            p.drawString(280,550+i*20,str(request_param_list[i].request_param_isnull))
            p.drawString(320,550+i*20,request_param_list[i].request_param_desc)

        p.drawString(50,250,"参数名")
        p.drawString(200,250,"参数类型")
        p.drawString(400,250,"说明")

        response_param_list = ResponseParam.objects.filter(interface__id = interface.id)
        for i in range(len(response_param_list)):
            p.drawString(50,200+i*20,response_param_list[i].response_param_name)
            p.drawString(200,200+i*20,response_param_list[i].response_param_type)
            p.drawString(400,200+i*20,response_param_list[i].response_param_desc)
        p.showPage()

    p.save()
    response.write(temp.getvalue())
    return response
