from django.db import models

#自定义管理器对象Manager
class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)


# Create your models here.
class BookInfo(models.Model):
    class Meta:
        db_table = 'bookinfo'
        verbose_name_plural = '书籍名'

    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    book1 = models.Manager()    #这个是原始的管理器
    book2 = BookInfoManager()   #这个是自定义的管理器


class HeroInfo(models.Model):
    class Meta:
        db_table = 'heroinfo'
        verbose_name_plural = '英雄人物'

    hname = models.CharField(max_length=20)
    hender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
