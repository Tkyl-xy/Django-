from django.shortcuts import render
from django.db import models
from .models import *

# Create your views here.
def index(request):
    bg = BookInfo.book1.filter(bread__gt=models.F('bcommet'))
    bg1 = BookInfo.book1.filter(bcommet__gt=models.F('bread'))
    # bc = BookInfo.book2.filter('bcommet')
    context = {
        'bg':bg,
        'bg1':bg1

        # 'bc':bc
    }
    '''
    查询集：
    F对象：
    要先导入
    from django.db.models import F
    可以使用模型的字段A与字段B进行比较，如果A写在了等号的左边，则B出现在等号的右边，需要通过F对象构造
    list.filter(bread__gte=F('bcommet'))
    django支持对F()对象使用算数运算
    list.filter(bread__gte=F('bcommet') * 2)
    F()对象中还可以写作“模型类__列名”进行关联查询
    list.filter(isDelete=F('heroinfo__isDelete'))
    对于date/time字段，可与timedelta()进行运算
    list.filter(bpub_date__lt=F('bpub_date') + timedelta(days=1))
    '''

    """
    Q对象
    要先导入
    过滤器的方法中关键字参数查询，会合并为And进行
    需要进行or查询，使用Q()对象
    Q对象(django.db.models.Q)用于封装一组关键字参数，这些关键字参数与“比较运算符”中的相同
    from django.db.models import Q
    list.filter(Q(pk_ _lt=6))
    Q对象可以使用&（and）、|（or）操作符组合起来
    当操作符应用在两个Q对象时，会产生一个新的Q对象
    list.filter(pk_ _lt=6).filter(bcommet_ _gt=10)
    list.filter(Q(pk_ _lt=6) | Q(bcommet_ _gt=10))
    使用~（not）操作符在Q对象前表示取反
    list.filter(~Q(pk__lt=6))
    """
    return render(request, 'index.html', context)


