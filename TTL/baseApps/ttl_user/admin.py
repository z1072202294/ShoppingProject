from django.contrib import admin
from .models import UserInfo


# Register your models here.
# class UserInfoAdmin(admin.ModelAdmin):
#     list_display = ['nickname', 'email', 'shou', 'address', 'youbian', 'phone']


admin.site.register(UserInfo)
