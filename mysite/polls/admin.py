from django.contrib import admin
from .models import Question,Choice,Intf,UserInfo,BlogBody

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']



admin.site.register(Question, QuestionAdmin)



class InterfaceAdmin(admin.ModelAdmin):

    fieldsets = [
        ('interface sn',                {'fields': ['interface_sn']}),
        ('interface name',              {'fields': ['interface_name']}),
        ('request method',              {'fields': ['request_method']}),
        ('request link',                {'fields': ['request_link']}),
        ('interface desc',              {'fields': ['interface_desc']}),
    ]
    list_display = ('interface_sn', 'interface_name', 'request_method','request_link','interface_desc')
    search_fields = ['interface_name']

admin.site.register(Intf, InterfaceAdmin)


class UserInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('nickname',{'fields': ['nickname']}),
        ('work', {'fields': ['work']}),
        ('company', {'fields': ['company']}),
        ('email', {'fields': ['email']}),
    ]
    list_display = ('nickname', 'work', 'company','email')
    search_fields = ['nickname']

admin.site.register(UserInfo, UserInfoAdmin)

class BlogBodyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('blog_title',{'fields': ['blog_title']}),
        ('blog_body', {'fields': ['blog_body']}),
        ('blog_type', {'fields': ['blog_type']}),
        ('blog_timestamp', {'fields': ['blog_timestamp']}),
        ('blog_imgurl', {'fields': ['blog_imgurl']}),
        ('blog_author', {'fields': ['blog_author']}),
    ]
    list_display = ('blog_title', 'blog_type','blog_timestamp','blog_imgurl','blog_author')
    search_fields = ['nickname']

admin.site.register(BlogBody, BlogBodyAdmin)
