from django.conf.urls import url
from . import views

app_name = 'blogs'
urlpatterns = [
    # url(r'^index/$',views.Index,name='index'),
    url(r'^index/(?P<page_num>[0-9]+)/$',views.page_index,name='page_index'),
    url(r'^article/(?P<blog_body_id>[0-9]+)/$', views.article, name='article'),
    url(r'^article/type/(?P<blog_typeid>[0-9]+)/$', views.type_article, name='type_article'),
    url(r'^add_article/', views.add_article, name='add_article'),
    url(r'^sub_article/', views.sub_article, name='sub_article'),
]