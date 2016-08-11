from django.shortcuts import render
from article.models import Article,Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from datetime import datetime
# Create your views here.

from django.http import  HttpResponse
from tools.forms import Addform


#通过视图返回
class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = "post_list"

    def get_queryset(self):
        post_list = Article.objects.all()
        return post_list

    #把分类的信息传到前面去
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('created_time')
        return super(HomeView, self).get_context_data(**kwargs)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articleDetail.html'
    context_object_name = 'articleDetail'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()

        return obj
    def get_context_data(self, **kwargs):

        kwargs['category_list'] = Category.objects.all().order_by('created_time')
        return super(ArticleDetailView, self).get_context_data(**kwargs)



class CategotyListView(ListView):

    template_name = 'home.html'
    context_object_name = "post_list"
    # 接收的参数是分类的id

    pk_url_kwarg = 'category_id'


    def get_queryset(self):
        article_list = Article.objects.filter(category=self.kwargs['category_id'])

        return article_list
    def get_context_data(self, **kwargs):
        
        context = super(CategotyListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all().order_by('created_time')
        return context




#//旧的方法直接返回
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