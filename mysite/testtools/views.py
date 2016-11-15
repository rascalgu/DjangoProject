# -*- coding: utf-8 -*-
from .models import Project,Category,Interface,RequestParam,ResponseParam
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

def Project_List(request):
    project_list = findProjectListAll()
    return render(request, 'testtools/interface_list.html',{'project_list': project_list})

def Project_List_ById(request,project_id):
    project_list = findProjectListAll()
    interface_list = findInterfaceListByProjectId(project_id)
    return render(request,'testtools/interface_list.html',{'project_list': project_list,'interface_list':interface_list})

def Ajax_Interface_List(request,project_id):
    interface_list = findInterfaceListByProjectId(project_id)
    return HttpResponse(interface_list)


def findCategoryByAll():
    category_list = Category.objects.all()
    return category_list

def findInterfaceByAll():
    interface_list = Interface.objects.all()
    return interface_list

def findInterfaceListById(category_id):
    # if category_id == '1':
    #     interface_list = Interface.objects.filter(Q(category_id=10000)|Q(category_id=50000))
    # else:
    interface_list = serializers.serialize("json",Interface.objects.filter(category_id = category_id))
    return interface_list

def findInterfaceDetailById(interface_id):
    interface_detail = Interface.objects.filter(id = interface_id)
    return interface_detail


def Index(request):
    return  render(request,'testtools/index.html')


def Interface_Test_Detail(request,interface_id):
    project_list = findProjectListAll()
    category_list = findCategoryByAll()
    interface_detail = findInterfaceDetailById(interface_id)
    return render(request,'testtools/interface_detail.html',{'interface_detail':interface_detail,'category_list': category_list,'project_list':project_list})


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
    return render(request,'testtools/interface_list.html',{'form':form})



def DataDesc(request):
    return render(request, 'testtools/datadesc.html')







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
