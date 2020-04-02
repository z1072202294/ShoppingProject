from django.db import models


# Create your models here.
class TypeInfo(models.Model):
    # 商品分类信息
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    title = models.CharField(max_length=20)  # 分类

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class GoodsInfo(models.Model):
    # 商品具体信息
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    title = models.CharField(max_length=20, unique=True)  # 商品名称
    img = models.ImageField(upload_to='图片路径')
    a = 123
