from django.shortcuts import render
from .models import Intf
from django.db.models import Q
# Create your views here.

def Index(request):
    category_list = Intf.objects.filter(upper = 0)
    return render(request, 'testtools/intfindex.html',{'category_list': category_list})

def IntfList(request,category_id):
    category_list = Intf.objects.filter(upper = 0)
    if category_id == '0':
        interface_list = Intf.objects.filter(Q(upper=10000)|Q(upper=50000))
    else:
        interface_list = Intf.objects.filter(upper = category_id)
    return render(request,'testtools/intfindex.html',{'interface_list':interface_list,'category_list': category_list})

def DataDesc(request):
    return render(request, 'testtools/datadesc.html')

def AutoDoc(request):
    category_list = Intf.objects.filter(upper = 0)
    interface_list = Intf.objects.filter(Q(upper=10000)|Q(upper=50000))
    return render(request, 'testtools/autodoc.html',{'category_list':category_list,'interface_list':interface_list})
