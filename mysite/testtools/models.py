# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200, null=True, blank=True,verbose_name='项目名称')
    def __unicode__(self):
        return self.project_name

class Category(models.Model):
    category_name = models.CharField(max_length=40, null=True, blank=True,verbose_name='类型名称')
    parent_id = models.IntegerField(null=True, blank=True,verbose_name='类型父id')
    x = models.IntegerField(null=True, blank=True,verbose_name='目录x坐标')
    y = models.IntegerField(null=True, blank=True,verbose_name='目录y坐标')
    category_desc = models.CharField(max_length=255, null=True, blank=True,verbose_name='目录描述')

    def __unicode__(self):
        return self.category_name


class Interface(models.Model):
    project = models.ForeignKey(Project,related_name='project_interface')
    category = models.ForeignKey(Category,related_name='category_interface')

    interface_sn = models.CharField(max_length=10, null=True, blank=True,verbose_name='接口编号')
    interface_name = models.CharField(max_length=200, null=True, blank=True,verbose_name='接口名称')
    request_method = models.CharField(max_length=20, null=True, blank=True,verbose_name='请求方法')
    request_link = models.CharField(max_length=255, null=True, blank=True,verbose_name='请求链接')

    request_sample = models.TextField(null=True, blank=True,verbose_name='请求样例')
    response_sample = models.TextField(null=True, blank=True,verbose_name='返回样例')
    request_desc = models.TextField(null=True, blank=True,verbose_name='请求描述')
    response_desc = models.TextField(null=True, blank=True,verbose_name='返回描述')

    def __unicode__(self):
        return self.interface_name

    class Meta:
            ordering = ['interface_sn']

class RequestParam(models.Model):
    interface = models.ForeignKey(Interface, related_name='interface_requestparam')

    request_param_name = models.CharField(max_length=200, null=True, blank=True,verbose_name='请求参数名称')
    request_param_type = models.CharField(max_length=20, null=True, blank=True,verbose_name='请求参数类型')
    request_param_isnull = models.IntegerField(verbose_name='请求参数是否必填')
    request_param_value = models.CharField(max_length=255,null=True,blank=True,verbose_name='请求参数值')
    request_param_desc = models.CharField(max_length=200, null=True, blank=True,verbose_name='请求参数描述')


    def __unicode__(self):
        return self.request_param_name


class ResponseParam(models.Model):
    interface = models.ForeignKey(Interface, related_name='interface_responseparam')

    response_param_name = models.CharField(max_length=200, null=True, blank=True,verbose_name='返回参数名称')
    response_param_type = models.CharField(max_length=20, null=True, blank=True,verbose_name='返回参数类型')
    response_param_desc = models.CharField(max_length=200, null=True, blank=True,verbose_name='返回参数描述')


    def __unicode__(self):
        return self.response_param_name

class TestScenarios(models.Model):

    project = models.ForeignKey(Project,related_name='project_testscenarios')
    interfaces = models.ManyToManyField(Interface,verbose_name=('相关接口'), related_name='interfaces_testscenarios', blank=True)


    test_scenario_name = models.CharField(max_length=200, null=True, blank=True,verbose_name='测试场景名称')
    test_scenario_type = models.IntegerField(verbose_name='测试场景类型')
    state = models.IntegerField(verbose_name='测试状态',default='0')
    createtime = models.DateTimeField( null=True, blank=True,auto_now_add = True,verbose_name='创建时间')
    updatetime = models.DateTimeField( null=True, blank=True,auto_now = True,verbose_name='更新时间')

    def __unicode__(self):
        return self.test_scenario_name

    class Meta:
            ordering = ['-createtime']

class Message(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True,verbose_name='姓名')
    Email = models.EmailField(null=True,blank=True)
    message = models.TextField(null=True,blank=True,verbose_name='留言')

    def __unicode__(self):
        return self.name