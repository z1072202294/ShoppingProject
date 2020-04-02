"""TTL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('ttl_user.urls'),name = 'ttl_user'),
    # path('order/',include('ttl_order.urls'),name = 'ttl_order'),
    path('goods/',include('ttl_goods.urls'),name = 'ttl_goods'),
    # path('cart/',include('ttl_cart.urls'),name = 'ttl_cart'),

]
