from django.contrib import admin

# Register your models here.
from myapp.models import student

# 簡易顯示
# admin.site.register(student)

# 顯示多個欄位、過濾、搜尋與排序
class studentAdmin(admin.ModelAdmin):
    list_display=('id','cName','cSex','cBirthday','cEmail','cPhone',)
    list_filter=('cSex',)
    search_fields=('cName','cEmail','cPhone',)
    ordering=('id','cName',)

admin.site.register(student, studentAdmin)