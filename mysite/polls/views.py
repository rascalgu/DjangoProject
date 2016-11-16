# -*- coding: utf-8 -*-
import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from .models import Question, Choice, UserInfo, BlogBody
from django.core.urlresolvers import reverse
from django.utils import timezone

from .forms import AddForm



# Create your views here.

# def index(request):
#     #latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     latest_question_list = Question.objects.all()
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'blogs/interface_list.html', context)

def testb(request):
    if request.method == 'POST':  # 当提交表单时

        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'polls/testb.html', {'form': form})


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))

def testa(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    List = map(str, range(100))# 一个长度为100的 List

    return  render(request,'polls/testa.html',{'string':string,'TutorialList':TutorialList,'info_dict':info_dict,'List':List})

def index(request):
    userinfo = UserInfo.objects.first()
    blog_body = BlogBody.objects.all()[:6]
    return render(request,'polls/index.html',{'userinfo': userinfo, 'blog_body': blog_body})

def article(request, blog_body_id=''):
    blog_content = BlogBody.objects.get(id=blog_body_id)
    return render(request, 'polls/view.html', {'blog_content': blog_content})

def python(request):
    sql = 'select id, blog_title, blog_type, blog_timestamp, blog_body from polls_blogbody WHERE blog_type = "Python"'
    python_blog = BlogBody.objects.raw(sql)
    return render(request, 'polls/python_list.html', {'python_blog': python_blog})

def add_article(request):
    return render(request, 'polls/add_article.html')

def sub_article(request):
    if request.method == 'GET':
        mytype = request.GET['article_type']
        title = request.GET['article_title']
        body = request.GET['article_editor']
        updb = BlogBody(blog_title=title, blog_body=body, blog_type=mytype, blog_timestamp=time.strftime("%Y-%m-%d %X", time.localtime()), blog_author='茶客大人')
        updb.save()
        return redirect('/blogs/'+mytype)

# class IndexView(generic.ListView):
#     template_name = 'pokks/interface_list.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'blogs/detail.html', {'question': question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'blogs/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('blogs:results', args=(p.id,)))
