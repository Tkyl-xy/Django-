from django.contrib import admin
from .import models

# Register your models here.
class HeroAdmin(admin.ModelAdmin):
    # list_display = ['id','hname','hcontent','hbook','hbook_id']

    list_filter = ['hname']

    search_fields = ['hname']

    list_per_page = 5

class BookAdmin(admin.ModelAdmin):
    # list_display = ['id','hname','hcontent','hbook','hbook_id']

    list_filter = ['btitle']

    search_fields = ['btitle']

    list_per_page = 5


admin.site.register(models.HeroInfo, HeroAdmin)
admin.site.register(models.BookInfo, BookAdmin)