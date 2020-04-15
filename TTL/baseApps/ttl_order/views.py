from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import order
# 订单页
def index(request):
    detail = order.objects.all()
    return render(request, 'order/order_up.html', {"index": detail})


# 订单详情
def detail(request):
    detail_list = order.objects.all()
    return render(request, 'order/show.html', {"detail": detail_list})
# 提交订单
# @user_decorator.login
def judgOrder(request):
    # uid = request.session['user_id']
    # user = order.objects.get(id=uid)
    # cart_ids = request.GET.getlist('cart_id')
    carts = []
    total_price = 0
    # for goods_id in cart_ids:
    #     cart = CartInfo.objects.get(id=goods_id)
    #     carts.append(cart)
    #     total_price = total_price + float(cart.count) * float(cart.goods.gprice)

    total_price = float('%0.2f' % total_price)
    trans_cost = 10  # 运费
    total_trans_price = trans_cost + total_price
    context = {
        'title': '提交订单',
        'page_name': 1,
        # 'user': user,
        'carts': carts,
        'total_price': float('%0.2f' % total_price),
        'trans_cost': trans_cost,
        'total_trans_price': total_trans_price,
        # 'value':value
    }
    return render(request, 'order/confrim.html', context)


