from django.db import models


class Article(models.Model):
    Article_State = {
        ('d','Draft'),
        ('p','Publish'),
    }

    title = models.CharField('标题',max_length=100)
    content = models.TextField('正文')
    create_time = models.DateField('创建时间',auto_now_add=True)
    last_revise_time = models.DateField('修改时间',auto_now=True)
    state = models.CharField('文章状态',max_length=1,choices=Article_State)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_revise_time']



