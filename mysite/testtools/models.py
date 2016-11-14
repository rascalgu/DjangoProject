from django.db import models


# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200, null=True, blank=True)
    def __unicode__(self):
        return self.project_name

class Category(models.Model):
    category_name = models.CharField(max_length=40, null=True, blank=True)
    parent_id = models.IntegerField(null=True, blank=True)
    x = models.IntegerField(null=True, blank=True)
    y = models.IntegerField(null=True, blank=True)
    category_desc = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.category_name


class Interface(models.Model):
    project = models.ForeignKey(Project,related_name='project_interface',default=1)
    category = models.ForeignKey(Category,related_name='category_interface')

    interface_sn = models.CharField(max_length=10, null=True, blank=True)
    interface_name = models.CharField(max_length=200, null=True, blank=True)
    request_method = models.CharField(max_length=20, null=True, blank=True)
    request_link = models.CharField(max_length=255, null=True, blank=True)

    request_sample = models.TextField(null=True, blank=True)
    response_sample = models.TextField(null=True, blank=True)
    request_desc = models.TextField(null=True, blank=True)
    response_desc = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.interface_name


class RequestParam(models.Model):
    interface = models.ForeignKey(Interface, related_name='interface_requestparam')

    request_param_name = models.CharField(max_length=200, null=True, blank=True)
    request_param_type = models.CharField(max_length=20, null=True, blank=True)
    request_param_isnull = models.IntegerField()
    request_param_desc = models.CharField(max_length=200, null=True, blank=True)


    def __unicode__(self):
        return self.request_param_name


class ResponseParam(models.Model):
    interface = models.ForeignKey(Interface, related_name='interface_responseparam')

    response_param_name = models.CharField(max_length=200, null=True, blank=True)
    response_param_type = models.CharField(max_length=20, null=True, blank=True)
    response_param_desc = models.CharField(max_length=200, null=True, blank=True)


    def __unicode__(self):
        return self.response_param_name
