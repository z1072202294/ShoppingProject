from django.test import TestCase

# Create your tests here.

# 添加购物车按钮
# from baseApps.ttl_cart.forms import CartAddProductForm
#
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})


# 商品相亲页添加
# <form action="{% url 'cart:cart_add' product.id %}" method="post">
#     {{ cart_product_form }}
#     {% csrf_token %}
#     <input type="submit" value="Add to cart">
# </form>