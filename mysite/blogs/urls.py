from django.conf.urls import url
from . import views

app_name = 'blogs'
urlpatterns = [
    url(r'^index/$',views.Index,name='index'),
    url(r'^article/(?P<blog_body_id>[0-9])/$', views.article, name='article'),
    url(r'^add_article/', views.add_article, name='add_article'),
    url(r'^sub_article/', views.sub_article, name='sub_article'),
]