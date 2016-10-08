from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return  self.choice_text


class Intf(models.Model):
    interface_sn = models.CharField(max_length=10)
    interface_name = models.CharField(max_length=80)
    request_method = models.CharField(max_length=10)
    request_link = models.CharField(max_length=255)
    interface_desc = models.CharField(max_length=255)

    def __str__(self):
        return self.interface_name


class UserInfo(models.Model):
    nickname = models.CharField(max_length=20)
    work = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    email = models.CharField(max_length=20)

class BlogBody(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_body = models.TextField()
    blog_type = models.CharField(max_length=50)
    blog_timestamp = models.DateTimeField()
    blog_imgurl = models.CharField(max_length=200, null=True)
    blog_author = models.CharField(max_length=20)

class Interface(models.Model):
    tree_id = models.IntegerField(default=0)
    tree_pid = models.IntegerField(default=0)
    tree_name = models.CharField(max_length=200)
    intf_name = models.CharField(max_length=50)
    intf_type = models.CharField(max_length=10)
    intf_link = models.CharField(max_length=255)

