from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('list(\d+)_(\d+)_(\d+)/', views.good_list, name="good_list"),
    path('(\d+)/', views.detail, name="detail"),
    path(r'search/', views.ordinary_search, name="ordinary_search"),  # 全文检索
]
