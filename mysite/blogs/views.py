# -*- coding: utf-8 -*-
import time

from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect,render_to_response
from django.views import generic
from .models import UserInfo,BlogBody
from django.core.urlresolvers import reverse
from django.utils import timezone

from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage


# Create your views here.

# def Index(request):
#     userinfo = UserInfo.objects.first()
#     blog_body = BlogBody.objects.all()[:6]
#     blog_type = BlogBody.objects.values('blog_typeid','blog_type').annotate(count=Count('blog_typeid')).order_by('blog_typeid')
#     return render(request,'blogs/index.html',{'userinfo': userinfo, 'blog_body': blog_body,'blog_type':blog_type})
def page_index(request,page_num):
    userinfo = UserInfo.objects.first()
    blog_body = BlogBody.objects.all()
    blog_type = BlogBody.objects.values('blog_typeid','blog_type').annotate(count=Count('blog_typeid')).order_by('blog_typeid')

    paginator = JuncheePaginator(blog_body,6)
    try:
        blog_body = paginator.page(page_num)
    except PageNotAnInteger:
        blog_body = paginator.page(1)
    except EmptyPage:
        blog_body = paginator.page(paginator.num_pages)
    return render_to_response('blogs/index.html',{'userinfo': userinfo, 'blog_body': blog_body,'blog_type':blog_type})

def article(request, blog_body_id=''):
    blog_content = BlogBody.objects.get(id=blog_body_id)
    return render(request, 'blogs/view.html', {'blog_content': blog_content})

def article(request, blog_body_id=''):
    blog_content = BlogBody.objects.get(id=blog_body_id)
    return render(request, 'blogs/view.html', {'blog_content': blog_content})

def type_article(request,blog_typeid=''):
    userinfo = UserInfo.objects.first()
    blog_type = BlogBody.objects.values('blog_typeid','blog_type').annotate(count=Count('blog_typeid')).order_by('blog_typeid')
    blog_body = BlogBody.objects.filter(blog_typeid=blog_typeid)[:6]
    return render(request,'blogs/index.html',{'userinfo':userinfo,'blog_body': blog_body,'blog_type':blog_type})

def add_article(request):
    return render(request, 'blogs/add_article.html')

def sub_article(request):
    if request.method == 'GET':
        mytype = request.GET['article_type']
        title = request.GET['article_title']
        body = request.GET['article_editor']
        updb = BlogBody(blog_title=title, blog_body=body, blog_type=mytype, blog_timestamp=time.strftime("%Y-%m-%d %X", time.localtime()), blog_author='茶客大人')
        updb.save()
        return redirect('/blogs/index')








class JuncheePaginator(Paginator):
    def __init__(self, object_list, per_page, range_num=5, orphans=0, allow_empty_first_page=True):
        Paginator.__init__(self, object_list, per_page, orphans, allow_empty_first_page)
        self.range_num = range_num

    def page(self, number):
        self.page_num = number
        return super(JuncheePaginator, self).page(number)

    def _page_range_ext(self):
        num_count = 2 * self.range_num + 1
        if self.num_pages <= num_count:
            return range(1, self.num_pages + 1)
        num_list = []
        num_list.append(self.page_num)
        for i in range(1, self.range_num + 1):
            if self.page_num - i <= 0:
                num_list.append(num_count + self.page_num - i)
            else:
                num_list.append(self.page_num - i)

            if self.page_num + i <= self.num_pages:
                num_list.append(self.page_num + i)
            else:
                num_list.append(self.page_num + i - num_count)
        num_list.sort()
        return num_list

    page_range_ext = property(_page_range_ext)


