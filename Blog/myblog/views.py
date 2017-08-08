from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
import markdown

# Create your views here.
def index(request):
    list = Post.objects.all()
    return render(request,'blog/index.html',context={
        'welcome':"测试网页",
        'post_list':list,
    })

def test(request):
    return HttpResponse("123123123")

def detail(request,pk):
    print(pk)
    post = get_object_or_404(Post, pk=pk)
    print(post)
    # 把postdata解析成markdown
    post.body = markdown.markdown(text=post.body,extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])

    return render(request,'blog/detail.html',context={
        'post':post
    })



