from django.db import models
from django.utils import timezone

# Create your models here.
class student(models.Model):
    # 選單,第一个元素是在模型上設置的實際值，第二個元素是可讀的顯示名稱
    SEX_CHOICES = [
        ('M', '男'),
        ('F', '女'),
    ]
    cName = models.CharField('姓名',max_length=20, null=False)
    cSex = models.CharField('性別',max_length=1, choices=SEX_CHOICES, default='M', null=False)
    cBirthday = models.DateField('生日',null=False)
    cEmail = models.EmailField('Email',max_length=100, blank=True, default='')
    cPhone = models.CharField('手機',max_length=50, blank=True, default='')
    cAddr = models.CharField('地址',max_length=255, blank=True, default='')
    last_modified = models.DateTimeField('最后修改日期', auto_now = True)  # auto_now=True 會在每次保存或更新對象時自動更新這個欄位
    created = models.DateTimeField('保存日期',default = timezone.now)

    # 打印這個學生對象（例如在Django的管理界面中）時，顯示的是學生的姓名 cName
    def __str__(self):
        return self.cName