from django.db import models

from django.conf import settings
# from ..ttl_goods.models import GoodsInfo

# Create your models here.

from ttl_goods.models import GoodsInfo
from ttl_user.models import UserInfo

class  CartInfo(models.Model):
    # 用户
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE,verbose_name='用户')
    # 商品
    goods = models.ForeignKey(GoodsInfo,on_delete=models.CASCADE,verbose_name='商品')
    # 数量
    count = models.IntegerField(verbose_name='',default=0)


    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.nickname+'购物车'
