from django.contrib import admin
from booktest import models

#实现了关联到新增加一个BookInfo这样动态的加载注册三个HeroInfo信息
#StackedInline是一行一行的显示的
'''
class HeroInfoInline(admin.StackedInline):
    model = models.HeroInfo
    extra = 3
'''
#TabularInline是表格的形式添加的
class HeroInfoInline(admin.TabularInline):
    model = models.HeroInfo
    extra = 3


#定义页面管理的类，用于优化页面布局管理
class BookInfoAdmin(admin.ModelAdmin):
    #list_display是展示
    list_display = ['id', 'btitle', 'bpub_date']
    #list_filter是过滤,在右侧
    list_filter = ['btitle']
    #search_fields搜索字段，搜索框会出现在上側
    search_fields = ['btitle']
    #分页,分页框会出现在下侧
    list_per_page = 1
    #这个属性分组，
    fieldsets = [
        ('标题',{'fields':['btitle']}),
        ('日期',{'fields':['bpub_date']}),
    ]
    inlines = [HeroInfoInline]


# Register your models here.
admin.site.register(models.BookInfo, BookInfoAdmin)
admin.site.register(models.HeroInfo)