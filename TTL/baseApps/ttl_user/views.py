from django.shortcuts import render
from django.views import View
from django.http import JsonResponse,HttpResponse

# from Demopycharm.My_first_django.淘乐乐.ShoppingProject.TTL.baseApps.ttl_user.utils import smFunc

# from TTL.baseApps.ttl_user.utils import smFunc

from ttl_user import smFunc


# import os,sys
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
# print(os.path)
# print(sys.path)
# os.environ['DJANGO_SETTTINGS_MODULE'] = 'TTL.settings'
# django.setup()

# sys.path.insert(0,os.path.join(BASE_DIR,'baseApps'))
# Create your views here.

class RegisterView(View, smFunc.User_opera):
    '''
        关注的constellation , stock , city
    '''

    get_pages_html = ""
    post_pages_html = ""

    def get(self,request):
        return HttpResponse('注册页面')
        # return render(request,self.get_pages_html)

    def post(self,request):
        res = self.decode_loads(request.body)
        print(res.values())
        self.judgAuth(res.values())
        # return JsonResponse('注册成功',safe=False)
        return render(request,self.post_pages_html)