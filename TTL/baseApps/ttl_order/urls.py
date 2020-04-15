from django.urls import path,re_path

from . import views

urlpatterns = [
    path('index/', views.index),
    path('detail/', views.detail),
    path('judgOrder/',views.judgOrder),
    # path('students/', views.sutdents),
    # path('gradesStudents/', views.gradesStudents),

]
# VALUES (1, '苹果', '4.2','1','2','3','4','5','6');