from django.urls import path,re_path

from . import views

urlpatterns = [
    # path('myApp', views.index),
    # path('grades/', views.grades),
    # path('students/', views.sutdents),
    path('login/', views.login),

]