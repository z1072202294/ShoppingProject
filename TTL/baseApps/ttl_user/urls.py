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
    # url(r'^login_handle/$', login_handle, name="login_handle"),
    # url(r'^info/$', info, name="info"),
    # url(r'^order/(\d+)$', order, name="order"),
    # url(r'^site/$', site, name="site"),
    # # url(r'^place_order/$', views.place_order),
    # url(r'^logout/$', logout, name="logout"),
]