from django.shortcuts import render
from article.models import Article
from datetime import datetime
# Create your views here.

from django.http import  HttpResponse

def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})

def detail(request, my_args):
    article = Article.objects.all()[int(my_args)]
    str = ('title = %s,content = %s,create_time = %s'%(article.title,article.content,article.create_time))

    return HttpResponse(str)

def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})