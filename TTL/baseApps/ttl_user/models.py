from django.db import models

# from ShoppingProject.TTL.baseApps.ttl_goods.models import GoodsInfo
# from baseApps.ttl_goods.models import GoodsInfo

<<<<<<< HEAD
=======

>>>>>>> 3291e5623542141157588034829e2f6ba0f012db
from ttl_goods.models import GoodsInfo
from datetime import datetime


# Create your models here.s
class UserInfo(models.Model):
    # 用户名
    nickname = models.CharField(max_length=20, unique=True)
    # 密码
    password = models.CharField(max_length=40)
    # 邮箱
    email = models.EmailField(unique=True, error_messages={'logo': 'Unique 不可以重复'})
    # 收货地址
    shou = models.TextField(max_length=5000, default='[]')
    # 邮编
    youbian = models.CharField(max_length=6, default='')
    # 手机号
    phone = models.CharField(max_length=11, default='', )
    objects = models.Manager()

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class GoodsBrowser(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户ID')
    goods = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name='商品ID')
    browser_time = models.DateTimeField(default=datetime.now, verbose_name='浏览时间')

    class Meat:
        verbose_name = '用户浏览记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}浏览记录{1}'.format(self.user.nickname, self.goods.goods_title)


