# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import UserInfo,BlogBody

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('昵称', {'fields': ['nickname']}),
        ('职业', {'fields': ['work']}),
        ('公司', {'fields': ['company']}),
        ('Email', {'fields': ['email']}),
    ]
    list_display = ('nickname', 'work', 'company', 'email')
    search_fields = ['nickname']


class BlogBodyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('博客标题', {'fields': ['blog_title']}),
        ('博客内容', {'fields': ['blog_body']}),
        ('博客类型', {'fields': ['blog_type']}),
        ('博客发表时间', {'fields': ['blog_timestamp']}),
        ('博客图片', {'fields': ['blog_imgurl']}),
        ('博客作者', {'fields': ['blog_author']}),
    ]
    list_display = ('blog_title', 'blog_body', 'blog_type', 'blog_timestamp','blog_imgurl','blog_author')
    search_fields = ['blog_title']

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(BlogBody, BlogBodyAdmin)
