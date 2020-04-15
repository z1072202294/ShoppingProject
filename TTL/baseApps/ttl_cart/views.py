from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from .models import *

# # Create your views here.
from ttl_user import views


# @views.login
def user_cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {
        'title': '购物车',
        'page_name': 1,
        'carts': carts
    }
    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=request.session['user_id']).count()
        # 求当前用户购买了几件商品
        return JsonResponse({'count': count})
    else:
        return render(request, 'ttl_cart/cart.html', context)



# @views.login
def edit(request,cart_id,count):
    data = {}
    try:
        cart = CartInfo.objects.get(pk = int(cart_id))
        cart.count = int(count)
        cart.save()
    except Exception:
        data['count'] = count
    return JsonResponse(data)


# @views.login
def delete(request,cart_id):
    data = {}
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data['ok'] = 1
    except:
        data['ok'] = 0
    return JsonResponse(data)

# from django.http import HttpResponseRedirect
# from django.shortcuts import reverse
#
#
# # 如果未登录则转到登陆页面
# def login(func):
#     def login_fun(request, *args, **kwargs):
#         if 'user_id' in request.session:
#             return func(request, *args, **kwargs)
#         else:
#             red = HttpResponseRedirect(reverse("df_user:login"))
#             red.set_cookie('url', request.get_full_path())
#             # 保证用户再登陆验证之后仍点击到希望的页面
#             return red
#     return login_fun
#
# """
# http://127.0.0.1:8000/200/?type=10
# request.path :表示当前路径，为/200/
# request.get_full_path():表示完整路径，为/200/?type=10
# """


# from django.views.decorators.http import require_POST
# from baseApps.ttl_goods.models import GoodsInfo


# from .cart import Cart
# from .forms import  CartAddProductForm
#
#
# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
#     return redirect('cart:cart_detail')
#
#
# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('cart:cart_detail')
#
# def cart_detail(request):
#     cart = Cart(request)
#     for item in cart:
#         item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
#     return render(request, 'cart/detail.html', {'cart': cart})
#
