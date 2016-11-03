# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Intf, Category, Interface, RequestParam, ResponseParam


# Register your models here.

class IntfAdmin(admin.ModelAdmin):
    fieldsets = [
        ('目录id', {'fields': ['category_id']}),
        ('目录名称', {'fields': ['category_name']}),
        ('是否有上级菜单', {'fields': ['upper']}),
        ('备注', {'fields': ['remark']}),
        ('接口编号', {'fields': ['interface_sn']}),
        ('接口名称', {'fields': ['interface_name']}),
        ('请求方式', {'fields': ['request_method']}),
        ('请求链接', {'fields': ['request_link']}),
        ('应答数据', {'fields': ['response_data']}),
        ('示例', {'fields': ['context']}),
        ('接口描述', {'fields': ['interface_desc']}),
    ]
    list_display = (
        'category_id', 'category_name', 'upper', 'remark', 'interface_sn', 'interface_name', 'request_method',
        'request_link', 'response_data', 'context', 'interface_desc',)
    search_fields = ['interface_name']


admin.site.register(Intf, IntfAdmin)


class InterfaceInline(admin.TabularInline):
    model = Interface
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('父目录id', {'fields': ['parent_id']}),
        ('目录名称', {'fields': ['category_name']}),
        ('目录横坐标', {'fields': ['x']}),
        ('目录宗坐标', {'fields': ['y']}),
        ('目录描述', {'fields': ['category_desc']}),
    ]
    list_display = ('parent_id', 'category_name', 'x', 'y', 'category_desc')
    search_fields = ['category_name']
    inlines = [InterfaceInline]


class RequestParamInline(admin.TabularInline):
    model = RequestParam
    extra = 1


class ResponseParamInline(admin.TabularInline):
    model = ResponseParam
    extra = 1


class InterfaceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['category']}),
        ('接口编号', {'fields': ['interface_sn']}),
        ('接口名称', {'fields': ['interface_name']}),
        ('请求方式', {'fields': ['request_method']}),
        ('请求链接', {'fields': ['request_link']}),
        ('请求示例', {'fields': ['request_sample']}),
        ('应答示例', {'fields': ['response_sample']}),
        ('请求描述', {'fields': ['request_desc']}),
        ('应答描述', {'fields': ['response_desc']}),
    ]
    list_display = (
        'interface_sn', 'interface_name', 'request_method', 'request_link')
    search_fields = ['interface_name']
    inlines = [RequestParamInline, ResponseParamInline]


class RequestParamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['interface']}),
        ('请求参数名字', {'fields': ['request_param_name']}),
        ('请求参数类型', {'fields': ['request_param_type']}),
        ('请求参数必填', {'fields': ['request_param_isnull']}),
        ('请求参数说明', {'fields': ['request_param_desc']}),

    ]
    list_display = ('request_param_name', 'request_param_type', 'request_param_isnull', 'request_param_desc')
    search_fields = ['request_param_name']


class ResponseParamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['interface']}),
        ('应答参数名', {'fields': ['response_param_name']}),
        ('应答参数类型', {'fields': ['response_param_type']}),
        ('应答参数说明', {'fields': ['response_param_desc']}),


    ]
    list_display = ('response_param_name', 'response_param_type', 'response_param_desc')
    search_fields = ['response_param_name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Interface, InterfaceAdmin)
admin.site.register(RequestParam, RequestParamAdmin)
admin.site.register(ResponseParam, ResponseParamAdmin)
