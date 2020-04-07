from django.contrib import admin

# Register your models here.
from .models import TypeInfo, GoodsInfo


class TpyeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']  # 显示id 和 分类名称
    search_fields = ['title']  # 查询
    list_display_links = ['title']  # 可以跳转


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'goods_title', 'goods_unit', 'goods_click',
                    'goods_jianjie', 'goods_price', 'goods_kucun']
    list_editable = ['goods_kucun']  # 可编辑的内容
    readonly_fields = ['goods_click']  # 只读内容
    search_fields = ['goods_title', 'goods_content', 'goods_jianjie']
    list_display_links = ['goods_title']


admin.site.register(TypeInfo, TpyeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
