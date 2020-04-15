# from django.db import models
# 
# 
# # Create your models here.
# class UserInfo(models.Model):
#     # 用户名
#     nickname = models.CharField(max_length=20, unique=True)
#     # 密码
#     password = models.CharField(max_length=32)
#     # 邮箱
#     email = models.EmailField(unique=True,error_messages={'logo':'Unique 不可以重复'})
#     # 收货地址
#     shou = models.CharField(max_length=100, default='')
#     # 邮编
#     youbian = models.CharField(max_length=6, default='')
#     # 手机号
#     phone = models.CharField(max_length=11, default='', )
#     objects = models.Manager()
# 
#     class Meta:
#         verbose_name = '用户信息'
#         verbose_name_plural = verbose_name
# 
#     def __str__(self):
#         return self.nickname
