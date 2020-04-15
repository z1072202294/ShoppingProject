from django.contrib import admin
from .models import CartInfo


# Register your models here.


class CartInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'goods', 'count']
    list_per_page = 5
    list_filter = ['user', 'goods', 'count']
    search_fields = ['user_name', 'goods__title']
    readonly_fields = ['user', 'goods', 'count']


admin.site.register(CartInfo, CartInfoAdmin)
