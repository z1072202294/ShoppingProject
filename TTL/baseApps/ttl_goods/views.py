from django.shortcuts import render,HttpResponse
# from ..ttl_user.models import UserInfo, GoodsBrowser
from .models import TypeInfo, GoodsInfo
# from ..ttl_cart.models import Cart


# Create your views here.
def index(request):
    type_list = TypeInfo.objects.all()
    print(type_list[1].GoodsINfo.objects.order_by('id'))
    # type0 = type_list[0].goodsinfo_set.oder_by('-id')[:4]
    return HttpResponse('ok')