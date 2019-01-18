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

    def __str__(self):
        return self.btitle

    book1 = models.Manager()    #这个是原始的管理器
    book2 = BookInfoManager()   #这个是自定义的管理器
    #第一种自定义创建模型对象
    @classmethod
    def create(cls, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b



class HeroInfo(models.Model):
    class Meta:
        db_table = 'heroinfo'
        verbose_name_plural = '英雄人物'


    hname = models.CharField(max_length=20)
    hender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    #我们关注 ordering 这个选项就够了。 如果你设置了这个选项，
    # 那么除非你检索时特意额外地使用了 order_by()，
    # 否则，当你使用 Django 的数据库 API 去检索时，
    # HeroInfo对象的相关返回值默认地都会按 name 字段排序。
    # def __unicode__(self):
    #     return self.hname
    def __str__(self):
        return self.hname

    '''
    --------------------------------------------------------------------------------------------------------------------
    这里是常用的{ 查询集 }
    In [6]: BookInfo.book2.values()返回的所有对象所构成的所有列表，然后把他们都呈现出来
    Out[6]: <QuerySet [
    {'id': 1, 'btitle': '射雕英雄传', 'bpub_date': datetime.datetime(1980, 5, 1, 0, 0, tzinfo=<UTC>), 'bread': 12, 'bcommet': 34, 'isDelete': False}, 
    {'id': 4, 'btitle': '雪山飞狐', 'bpub_date': datetime.datetime(1987, 11, 11, 0, 0, tzinfo=<UTC>), 'bread': 58, 'bcommet': 24, 'isDelete': False}, 
    {'id': 5, 'btitle': '斗破苍穹', 'bpub_date': datetime.datetime(2015, 10, 9, 16, 0, tzinfo=<UTC>), 'bread': 0, 'bcommet': 0, 'isDelete': False}, 
    {'id': 6, 'btitle': '小鱼儿与花无缺', 'bpub_date': datetime.datetime(2012, 12, 31, 16, 0, tzinfo=<UTC>), 'bread': 0, 'bcommet': 0, 'isDelete': False}]>


    In [7]: BookInfo.book2.all()返回的所有对象
    Out[7]: <QuerySet [<BookInfo: BookInfo object (1)>, <BookInfo: BookInfo object (4)>, <BookInfo: BookInfo object (5)>, <BookInfo: BookInfo object (6)>]>

    .count()返回当前查询的总条数
    In [10]: BookInfo.book2.count()
    Out[10]: 4
        
    #.exists()检查当前集合是否有数据，有数据返回True，否则返回False
    In [14]: BookInfo.book2.exists()
    Out[14]: True

    '''

    """
    ---------------------------------------------------------------------------------------------------------------
    { 限制查询集 }限制返回的数据
    查询集返回列表，可以使用下标的方式进行限制，等同于sql中的limit和offset子句
    In [33]: HeroInfo.objects.all()[0:2]
    Out[33]: <QuerySet [<HeroInfo: HeroInfo object (1)>, <HeroInfo: HeroInfo object (2)>]>

    In [32]: HeroInfo.objects.order_by('hname')[0:2]
    Out[32]: <QuerySet [<HeroInfo: HeroInfo object (13)>, <HeroInfo: HeroInfo object (6)>]>
    
    
    #更新单个对象可以在shell下进行更新
    In [41]: H = HeroInfo.objects.get(hname="胡斐")
    In [43]: H.hname = "叶斐"
    In [44]: H.save()
    这等同于如下SQL语句：
    SELECT id, name, address, city, state_province, country, website
    FROM books_publisher
    WHERE name = 'Apress';
    
    UPDATE books_publisher SET
        hname = '胡斐',
        hender = '1',
        isDelete = '0',
        hcontent = '胡家刀法',
        country = 'U.S.A.',
        hbook_id = '4'
    WHERE id = 52;
    在这个例子里我们可以看到Django的save()方法更新了不仅仅是hame列的值，
    还有更新了所有的列。 
    若hname以外的列有可能会被其他的进程所改动的情况下，
    只更改hname列显然是更加明智的。 
    """

    '''
    字段查询：
    实现where子名，作为方法fifter()、exclude()、get()的参数
    语法：属性名称__比较运算符=值
    表示两个下划线，左侧是属性名，右侧是比较类型
    ---------------------------------------------------------------------------------------------------------
    exact：表示判等，大小写敏感；如果没有写“ 比较运算符”，表示判等
    filter(hbook_id__exact=1)
    contains：是否包含，大小写敏感
    exclude(btitle__contains='传')
    startswith、endswith：以value开头或结尾，大小写敏感
    exclude(btitle__endswith='传')
    isnull、isnotnull：是否为null
    filter(btitle__isnull=False)
    在前面加个i表示不区分大小写，如iexact、icontains、istarswith、iendswith
    在前面加个i表示不区分大小写，如iexact、icontains、istarswith、iendswith
    in：是否包含在范围内
    
    
    filter(pk__in=[1, 2, 3, 4, 5])
    gt、gte、lt、lte：大于、大于等于、小于、小于等于
    filter(id__gt=3)
    
    
    year、month、day、week_day、hour、minute、second：对日期间类型的属性进行运算
    filter(bpub_date__year=1980)
    filter(bpub_date__gt=date(1980, 12, 31))
    
    跨关联关系的查询：处理join查询
    语法：模型类名 <属性名> <比较>
    注：可以没有__<比较>部分，表示等于，结果同inner join
    可返向使用，即在关联的两个模型中都可以使用
    In [89]: BookInfo.book1.filter(heroinfo__hcontent__contains='八').values()
    Out[89]: <QuerySet [{'id': 1, 'btitle': '射雕英雄传', 'bpub_date': datetime.datetime(1980, 5, 1, 0, 0, tzinfo=<UTC>), 'bread': 12, 'bcommet': 34, 'isDelete': False}, {'id': 2, 'bti
    tle': '天龙八部', 'bpub_date': datetime.datetime(1986, 7, 24, 0, 0, tzinfo=<UTC>), 'bread': 36, 'bcommet': 40, 'isDelete': True}]>
    
    --------------------------------------------------------------------------------------------        
    聚合函数
    使用aggregate()函数返回聚合函数的值
    函数：Avg，Count，Max，Min，Sum
    
    In [13]: avgId = BookInfo.book1.aggregate(models.Avg('id'))
    In [14]: avgId
    Out[14]: {'id__avg': Decimal('3.5000')}
    
    In [15]: sumId = BookInfo.book1.aggregate(models.Sum('id'))
    In [16]: sumId
    Out[16]: {'id__sum': Decimal('21')}
    
    In [17]: maxId = BookInfo.book1.aggregate(models.Max('id'))
    In [18]: maxId
    Out[18]: {'id__max': 6}
    
    

    '''


