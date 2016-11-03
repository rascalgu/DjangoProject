# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Intf
from .models import Category
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

def Index(request):
    category_list = Category.objects.filter(Q(x__gte = 0),Q(y = 0))
    return render(request, 'testtools/intfindex.html',{'category_list': category_list})

def IntfList(request,category_id):
    category_list = Category.objects.filter(Q(x__gte = 0),Q(y = 0))

    if category_id == '0':
        interface_list = Intf.objects.filter(Q(upper=10000)|Q(upper=50000))
    else:
        interface_list = Intf.objects.filter(upper = category_id)

    if (category_id == '10000'):
            subcategory = Category.objects.filter(Q(x = 1),Q(y__gt = 0))
    else :
            subcategory = Category.objects.filter(Q(x = 2),Q(y__gt = 0))
    return render(request,'testtools/intfindex.html',{'interface_list':interface_list,'category_list': category_list,'subcategory':subcategory})

def DataDesc(request):
    return render(request, 'testtools/datadesc.html')

def AutoDoc(request):
    category_list = Intf.objects.filter(upper = 0)
    interface_list = Intf.objects.filter(Q(upper=10000)|Q(upper=50000))
    return render(request, 'testtools/autodoc.html',{'category_list':category_list,'interface_list':interface_list})

def ToPdf(request):

    rl_config.warnOnMissingFontGlyphs = 0
    path ="D:\\Program Files\\Python\\Lib\\site-packages\\reportlab\\fonts"
    pdfmetrics.registerFont(TTFont('hei',os.path.join(path, 'simhei.ttf')))

    addMapping('cjk',0,0,'hei')

    response = HttpResponse(content_type='application/pdf')
    # #response['Content-Disposition'] = 'attachment; filename="大数据交易中心接口文档.pdf"'

    temp = StringIO()
    p = canvas.Canvas(temp)

    interface_list=Intf.objects.filter(Q(upper=10000)|Q(upper=50000))
    for intf in interface_list:
        p.setFont('hei',16)
        p.drawString(50,800,intf.interface_sn)
        p.drawString(100,800,intf.interface_name)
        p.drawString(50,780,"请求方式:")
        p.drawString(125,780,intf.request_method)
        p.drawString(50,760,"请求url:")
        p.drawString(50,740,intf.request_link)
        p.showPage()

    p.save()
    response.write(temp.getvalue())
    return response
