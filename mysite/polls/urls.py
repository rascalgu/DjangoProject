from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /blogs/
    url(r'^$', views.index, name='index'),

    url(r'^article/(?P<blog_body_id>[0-9])/$', views.article, name='article'),

    url(r'^python/',views.python,name ='python'),

    url(r'^add_article/', views.add_article, name='add_article'),
    url(r'^sub_article/', views.sub_article, name='sub_article'),

    # url(r'^$', views.IndexView.as_view(), name='index'),
    # # ex: /blogs/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /blogs/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /blogs/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^testa/', views.testa, name='testa'),
    url(r'^testb/', views.testb, name='testb'),
    url(r'^add/', views.add, name='add'),

]
