from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from django import forms
from .models import UserInfo
from . import smFunc

# from Demopycharm.My_first_django.淘乐乐.ShoppingProject.TTL.baseApps.ttl_user.utils import smFunc
# from TTL.baseApps.ttl_user.utils import smFunc



import inspect

def get__function_name():
    '''获取正在运行函数(或方法)名称'''
    return inspect.stack()[1][3]


GET_PAGES_HTML = "ttl_user/register.html"
# Create your views here.


class RegisterView(View, smFunc.RegisOpera):
    '''
        dispose registerPages requests
    '''

    def get(self,request):

        content = {"REGIS":self.__class__.__name__}
        return render(request,GET_PAGES_HTML,context=content)

    def post(self,request):
        res = request.POST
        print("=======post",res)
        res1 = request.body
        print("========body",res1)
        back_v = self.disposePost(res)
        if back_v != self.REDIRECT:
            return JsonResponse(back_v, safe=False)

        back_v["redirect"] = reverse("login")
        print(back_v)
        return JsonResponse(back_v,safe=False)


# #表单
# from django.shortcuts import render
# from django.http import HttpResponse,HttpResponseRedirect
# from django.template import RequestContext
# from django import forms
# from .models import UserInfo
#
# class UserForm(forms.Form):
#     username = forms.CharField(label='用户名',max_length=100)
#     password = forms.CharField(label='密码',widget=forms.PasswordInput())



def login(request):

    REDIRECT = {}
    FAIL = 0

    if request.method == 'POST':
        res = request.POST
        backv = smFunc.loginOpera(res)
        if backv:
            REDIRECT["redirect"] = reverse("index")
            return JsonResponse(REDIRECT,safe=False)

        return JsonResponse(FAIL,safe=False)

    else:
        print("======================get")
        # uf = UserForm()
        print(get__function_name())
        print(type(get__function_name()))
        content = {"LOGIN":get__function_name()}
        return render(request,GET_PAGES_HTML,context=content)




#登陆成功
def index(req):
    username = req.COOKIES.get('nickname','')

    return render('ttl_user/index.html' ,{'nickname':username})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('nickname')

    return response