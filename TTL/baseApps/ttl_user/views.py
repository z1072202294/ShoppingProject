from django.shortcuts import render
from django.views import View
from django.http import JsonResponse,HttpResponse
from django.template import loader

# from Demopycharm.My_first_django.淘乐乐.ShoppingProject.TTL.baseApps.ttl_user.utils import smFunc

# from TTL.baseApps.ttl_user.utils import smFunc

from ttl_user import smFunc
import hashlib,os,sys

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
        # sys.path.pop(0)
        # print(sys.path)

        content_text = {'comman':'w'}
        return render(request,"ttl_user/register.html",content_text)
        # return HttpResponse('注册页面')

    def post(self,request):
        '''
        nickname,password,email,show,youbian,phone
        '''
        res = request.body
        print(type(res))

        if res['password1'] != res['password2']:
            return JsonResponse('密码不一样',safe=False)

        back_v = self.judgAuth(res)
        return JsonResponse(back_v,safe=False)
        # return render(request,self.post_pages_html)