from django.db import models


# Create your models here.
class TypeInfo(models.Model):
    # 商品分类信息
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    title = models.CharField(max_length=20, verbose_name='商品分类')  # 分类

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class GoodsInfo(models.Model):
    # 商品具体信息
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    goods_title = models.CharField(max_length=20, unique=True, verbose_name='商品名称')  # 商品名称
    goods_image = models.ImageField(verbose_name='商品图片', upload_to='df_goods/image/%Y/%m', null=True, blank=True)  # 商品图片
    goods_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='商品价格')  # 商品价格
    goods_unit = models.CharField(max_length=20, default='230g', verbose_name='单个商品重量')  # 商品重量
    goods_click = models.IntegerField(verbose_name='点击量', default='0', null=False)
    goods_jianjie = models.CharField(max_length=200, verbose_name='商品简介')
    goods_kucun = models.IntegerField(verbose_name='商品库存', default=0)
    goods_content = models.TextField(verbose_name='商品详情')
    goods_type = models.ForeignKey(TypeInfo, on_delete=models.CASCADE, verbose_name='商品分类')

    class Meat:
        verbose_name = '具体商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_title
