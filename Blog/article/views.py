from django.shortcuts import render
from article.models import Article
from datetime import datetime
# Create your views here.

from django.http import  HttpResponse
from tools.forms import Addform

def home(request):

    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})

def detail(request,id):
    article = Article.objects.all()[int(id)]
    return render(request, 'articleDetail.html', {'post': article})


def test(request):
    if request.method == 'POST':
        form = Addform(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = Addform()

    return render(request, 'test.html', {'form': form})

def add(request):
    #表单提交
    # a = request.GET.get('a',0)
    # b = request.GET.get('b',0)
    # c = int(a)+int(b)
    #Django的forms提交
    if request.method == 'POST':
        form = Addform(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = Addform()

    return render(request, 'test.html', {'form': form})