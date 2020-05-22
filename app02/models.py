from django.db import models

# Create your models here.


class Entry(models.Model):

    name = models.CharField(max_length=128, verbose_name='网站信息')

    img = models.CharField(max_length=100,null=True, blank=True, verbose_name='网页配图')

    url = models.CharField(max_length=256,verbose_name='网页地址')

    source = models.CharField(max_length=100, blank=True, null=True, verbose_name='网页来源')

    visiting = models.PositiveIntegerField(default=0, verbose_name='网页访问量')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


    def increase_visiting(self):
        self.visiting += 1
        self.save(update_fields=['visiting'])



class CtrImplied(models.Model):

    Acceptno = models.CharField(max_length=128, verbose_name='受理号')

    Drugname = models.CharField(max_length=128, verbose_name='药品名称')

    Corpname = models.CharField(max_length=128, verbose_name='申请人名称')

    Indication = models.CharField(max_length=128, verbose_name='适应症')

    Register_Type = models.CharField(max_length=128, verbose_name='注册分类')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    Uptime = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')

    def __str__(self):
        return self.Acceptno


