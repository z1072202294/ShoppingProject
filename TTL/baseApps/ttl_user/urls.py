<<<<<<< HEAD
=======
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url


# from . import views
# from TTL.baseApps.ttl_user import views
from . import views

urlpatterns = [
    path(r'register/', views.RegisterView.as_view(), name="register"),
    # url(r'^register_handle/$', register_handle, name="register_handle"),
    # url(r'^register_exist/$', register_exist, name="register_exist"),
    path(r'login/', views.login, name="login"),
    url(r'^login_out/$', views.logout, name="logout"),
    url(r'^center/$', views.UserCenterView.as_view(), name="center"),
    url(r'^shou/$', views.Shou.as_view(), name="shou"),
    url(r'^shou/modify/$', views.shouModify, name="shouModify"),
    # url(r'^order/(\d+)$', order, name="order"),
    # url(r'^site/$', site, name="site"),
    # # url(r'^place_order/$', views.place_order),
    # url(r'^logout/$', logout, name="logout"),
]
>>>>>>> 645714608c9093b20d7b9df3bee8fc8110c61baa
