<<<<<<< HEAD
from django.contrib import admin
# from .models import UserInfo


# Register your models here.
# class UserInfoAdmin(admin.ModelAdmin):
#     list_display = ['nickname', 'email', 'shou', 'address', 'youbian', 'phone']


# admin.site.register(UserInfo)
=======
from django.contrib import admin
from .models import UserInfo


# Register your models here.
# class UserInfoAdmin(admin.ModelAdmin):
#     list_display = ['nickname', 'email', 'shou', 'address', 'youbian', 'phone']


admin.site.register(UserInfo)
>>>>>>> 645714608c9093b20d7b9df3bee8fc8110c61baa
