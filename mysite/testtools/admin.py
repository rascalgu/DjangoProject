from django.contrib import admin

from .models import Intf
# Register your models here.

class InterfaceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('目录id',{'fields': ['category_id']}),
        ('目录名称',{'fields': ['category_name']}),
        ('上级目录',{'fields': ['upper']}),
        ('备注', {'fields': ['remark']}),
        ('接口编号',{'fields': ['interface_sn']}),
        ('接口名称',{'fields': ['interface_name']}),
        ('请求方式',{'fields': ['request_method']}),
        ('请求链接',{'fields': ['request_link']}),
        ('返回数据',{'fields': ['response_data']}),
        ('上下文接口', {'fields': ['context']}),
        ('接口描述',{'fields': ['interface_desc']}),
    ]

    list_display = ('category_id','category_name','upper','remark','interface_sn','interface_name','request_method', 'request_link','response_data','context','interface_desc')
    search_fields = ['interface_name']
admin.site.register(Intf,InterfaceAdmin)