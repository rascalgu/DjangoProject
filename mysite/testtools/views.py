from django.shortcuts import render
from django.views import generic
from .models import Intf
# Create your views here.



# class IntfIndexView(generic.ListView):
#     template_name = 'testtools/intfindex.html'
#     context_object_name = 'latest_intf_list'
#
#     def get_queryset(self):
#         return Intf.objects.all()

def IntfIndex(request):
    category_list = Intf.objects.filter(upper = 0)
    return render(request, 'testtools/intfindex.html',
                  {'category_list': category_list})

def IntfList(request,category_id):
    single_interface_list = Intf.objects.filter(upper = category_id)
    return render(request, 'testtools/intfindex.html',
                  {'single_interface_list':single_interface_list})


def DataDesc(request):
    return render(request, 'testtools/datadesc.html')
