# -*- coding: utf-8 -*-
import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from .models import UserInfo,BlogBody
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your views here.

def Index(request):
    userinfo = UserInfo.objects.first()
    blog_body = BlogBody.objects.all()[:6]
    return render(request,'blogs/index.html',{'userinfo': userinfo, 'blog_body': blog_body})

def article(request, blog_body_id=''):
    blog_content = BlogBody.objects.get(id=blog_body_id)
    return render(request, 'blogs/view.html', {'blog_content': blog_content})


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