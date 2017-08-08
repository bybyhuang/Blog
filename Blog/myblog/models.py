from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='分类名称')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100,verbose_name='标签名称')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70,verbose_name='文章标题');
    body = models.TextField(verbose_name='文章内容')
    created_time = models.DateTimeField(verbose_name='创建时间');
    modified_time = models.DateTimeField(verbose_name='修改时间')
#     文章的摘要
    excerpt = models.CharField(max_length=100,blank=True,verbose_name='文章摘要')
    category = models.ForeignKey(Category,verbose_name='分类')
    tag = models.ManyToManyField(Tag,verbose_name='标签')
    user = models.ForeignKey(User,verbose_name='用户')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('myblog:detail',kwargs={'pk':self.pk})

# 管理员用户名 密码 admin  admin1234



