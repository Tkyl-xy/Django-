from django.db import models

#自定义管理器对象Manager
class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)
    #第二种方法是在自定义管理器中创建对象的对象方法
    def create(cls, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b


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
    # #第一种自定义创建模型对象
    # @classmethod
    # def create(cls, btitle, bpub_date):
    #     b = BookInfo()
    #     b.btitle = btitle
    #     b.bpub_date = bpub_date
    #     b.bread = 0
    #     b.bcommet = 0
    #     b.isDelete = False
    #     return b



class HeroInfo(models.Model):
    class Meta:
        db_table = 'heroinfo'
        verbose_name_plural = '英雄人物'

    hname = models.CharField(max_length=20)
    hender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
