from django.db import models

# Create your models here.


class Intf(models.Model):

    category_id = models.IntegerField()
    category_name = models.CharField(max_length=200,null=True,blank=True)
    upper = models.IntegerField()
    remark = models.TextField(null=True,blank=True)

    interface_sn = models.CharField(max_length=10,null=True,blank=True)
    interface_name = models.CharField(max_length=200,null=True,blank=True)
    request_method = models.CharField(max_length=20,null=True,blank=True)
    request_link = models.CharField(max_length=255,null=True,blank=True)
    response_data = models.TextField(null=True,blank=True)
    context = models.CharField(max_length=255,null=True,blank=True)
    interface_desc = models.CharField(max_length=255,null=True,blank=True)

    def __unicode__(self):
        return self.interface_name



