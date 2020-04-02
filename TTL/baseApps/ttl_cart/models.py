from django.db import models
from django.conf import settings
# from ..ttl_goods.models import GoodsInfo

# Create your models here.


class  Cart:

    def __init__(self,request):
        """
        初始化购物车
        :param request:
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # session中保存空白购物车数据
            cart = settings.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # def add(self, product, quantity=1, update_quantity=False):
    #     """
    #     向购物车中增加商品或者更新购物车中的数量
    #     """
    #
    #     product_id = str(product.id)
    #     if product_id not in self.cart:
    #         self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
    #     if update_quantity:
    #         self.cart[product_id]['quantity'] = quantity
    #     else:
    #         self.cart[product_id]['quantity'] += quantity
    #     self.save()


