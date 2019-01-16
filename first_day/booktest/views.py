from django.shortcuts import render
from .models import *

# Create your views here.
# from django.http import HttpResponse
# from django.template import RequestContext, loader

def index(request):
    #temp加载模板
    # temp = loader.get_template('index.html')
    #render是渲染模板，把模板从html中显示
    # return HttpResponse(temp.render())
    bookList = BookInfo.objects.all()
    context = {'list':bookList}
    return render(request, 'index.html', context)

def show(request,id):
    #这里找到bookID的信息
    book = BookInfo.objects.get(pk=id)
    #这里的book.heroinfo_set是书获取全部关联到的英雄属性；这是一对多的
    #这里的book.heroinfo_set是书对象的所有属性，这里是Django内部识别的写法
    herolist = book.heroinfo_set.all()

    #还有英雄对应书的对象hero.book；这个是一对一的

    context = {'list': herolist}
    return render(request, 'show.html', context)
