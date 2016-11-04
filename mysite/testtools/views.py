# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Intf,Category,Interface,RequestParam,ResponseParam
from django.db.models import Q

from django.http import HttpResponse
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

import os

def findCategoryByAll():
    category_list = Category.objects.all()
    return category_list

def findInterfaceByAll():
    interface_list = Interface.objects.all()
    return interface_list

def findInterfaceById(category_id):
    if category_id == '1':
        interface_list = Interface.objects.filter(Q(category_id=10000)|Q(category_id=50000))
    else:
        interface_list = Interface.objects.filter(category_id = category_id)
    return interface_list

def Interface_Test_Index(request):
    category_list = findCategoryByAll()
    interface_list = findInterfaceByAll()
    return render(request, 'testtools/index.html',{'category_list': category_list,'interface_list':interface_list})

def Interface_Test_List(request,category_id):
    category_list = findCategoryByAll()
    interface_list = findInterfaceById(category_id)
    return render(request,'testtools/index.html',{'interface_list':interface_list,'category_list': category_list})

def AutoDoc(request):
    category_list = findCategoryByAll()
    interface_list = findInterfaceByAll()
    return render(request, 'testtools/autodoc.html',{'category_list':category_list,'interface_list':interface_list})


def DataDesc(request):
    return render(request, 'testtools/datadesc.html')


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
