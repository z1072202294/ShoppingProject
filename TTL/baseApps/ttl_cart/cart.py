# from decimal import Decimal
# from django.conf import settings
# from baseApps.ttl_goods.models import GoodsInfo
#
# # Create your models here.
#
#
# class Cart:
#
#     def __init__(self,request):
#         """
#         初始化购物车
#         :param request:
#         """
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)
#         if not cart:
#             # session中保存空白购物车数据
#             cart = settings.session[settings.CART_SESSION_ID] = {}
#         self.cart = cart
#
#     def add(self, product, quantity=1, update_quantity=False):
#         """
#         向购物车中增加商品或者更新购物车中的数量
#         product:商品id,
#         quantity: 商品数量,默认1
#         update_quantuty:布尔值 ture将商品数量跟新为quantity的值,false将当钱数量增加quantity的值
#         """
#
#         product_id = str(product.id)
#         if product_id not in self.cart:
#             self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
#         if update_quantity:
#             self.cart[product_id]['quantity'] = quantity
#         else:
#             self.cart[product_id]['quantity'] += quantity
#         self.save()
#
#     def save(self):
#         # 设置session.modified的值为True，中间件在看到这个属性的时候，就会保存session
#         self.session.modified = True
#
#
#     def remove(self,product):
#         """
#         从购物车删除商品
#         根据id 删除
#         :return:
#         """
#         product_id = str(product.id)
#         if product_id in self.cart:
#             del self.cart['product_id']
#             self.save()
#
#     def __iter__(self):
#         """
#         遍历所有购物车中的商品并从数据库中取得商品对象
#         """
#         product_ids = self.cart.keys()
#         # 获取购物车内的所有商品对象
#         products = Product.objects.filter(id__in=product_ids)
#
#         cart = self.cart.copy()
#         for product in products:
#             cart[str(product.id)]['product'] = product
#
#         for item in cart.values():
#             item['price'] = Decimal(item['price'])
#             item['total_price'] = item['price'] * item['quantity']
#             yield item
#
#     def __len__(self):
#         """
#         购物车内一共有几种商品
#         """
#         return sum(item['quantity'] for item in self.cart.values())
#
#     def get_total_price(self):
#         return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
#
#     def clear(self):
#         del self.session[settings.CART_SESSION_ID]
#         self.save()