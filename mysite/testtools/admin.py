# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Project, Category, Interface, RequestParam, ResponseParam,TestScenarios,Message


# Register your models here.

class InterfaceInline(admin.TabularInline):
    model = Interface
    extra = 1

class TestScenariosInline(admin.TabularInline):
    model = TestScenarios
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('项目名称', {'fields': ['project_name']}),
    ]
    search_fields = ['category_name']
    inlines = [InterfaceInline,TestScenariosInline]

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
        (None, {'fields': ['project']}),
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

class TestScenariosAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['project']}),
        (None, {'fields': ['interfaces']}),
        ('测试场景名称', {'fields': ['test_scenario_name']}),
    ]
    list_display = ('test_scenario_name', 'test_scenario_type')
    search_fields = ['test_scenario_name']

class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('姓名', {'fields': ['name']}),
        ('Email', {'fields': ['Email']}),
        ('留言', {'fields': ['message']}),
    ]
    list_display = ('name', 'Email','message')
    search_fields = ['name']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Interface, InterfaceAdmin)
admin.site.register(RequestParam, RequestParamAdmin)
admin.site.register(ResponseParam, ResponseParamAdmin)
admin.site.register(TestScenarios,TestScenariosAdmin)
admin.site.register(Message,MessageAdmin)
