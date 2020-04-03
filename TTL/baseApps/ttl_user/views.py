<<<<<<< HEAD
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


class RegisterView(View, smFunc.User_opera):
    '''
        dispose registerPages requests
    '''
    # GET_PAGES_HTML = "ttl_user/register.html"

    def get(self,request):

        content = {"register":self.__class__.__name__}
        # content = {"judg":''}
        return render(request,GET_PAGES_HTML,context=content)

    def post(self,request):
        print('post')
        res = request.body
        print(res)
        print(type(res))
        # if res['password1'] != res['password2']:
        #     return JsonResponse('密码不一样',safe=False)

        # back_v = self.judgAuth(res)
        return HttpResponse(res)
        # return JsonResponse(back_v,safe=False)
        # return render(request,self.post_pages_html)



#表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=20)
=======
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from .models import UserInfo

#表单
class UserForm(forms.Form): 
    username = forms.CharField(label='用户名',max_length=100)
>>>>>>> 06534878862051449519ecf1deeb881859e3e735
    password = forms.CharField(label='密码',widget=forms.PasswordInput())


#登陆
<<<<<<< HEAD
def login(request):
    if request.method == 'POST':
        print('======Post')
        uf = UserForm(request.POST)
=======
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
>>>>>>> 06534878862051449519ecf1deeb881859e3e735
        if uf.is_valid():
            #获取表单用户密码
            nickname = uf.cleaned_data['nickname']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
<<<<<<< HEAD
            user = UserInfo.objects.filter(username__exact = nickname,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/user/register/')
=======
            user = UserInfo.objects.filter(nickname = nickname,password = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/register/')
>>>>>>> 06534878862051449519ecf1deeb881859e3e735
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('nickname',nickname,3600)
                return response
            else:
                #比较失败，还在login
<<<<<<< HEAD
                return HttpResponseRedirect('/user/login/')
    else:
        print("===get")
        # uf = UserForm()
        print(get__function_name())
        print(type(get__function_name()))
        content = {"login":get__function_name()}
        return render(request,GET_PAGES_HTML,context=content)

=======
                return HttpResponseRedirect('/user/')
    else:
        uf = UserForm()
    return render('log.html',{'uf':uf})
>>>>>>> 06534878862051449519ecf1deeb881859e3e735

#登陆成功
def index(req):
    username = req.COOKIES.get('nickname','')
<<<<<<< HEAD
    return render('ttl_user/index.html' ,{'nickname':username})
=======
    return render('index.html' ,{'nickname':username})
>>>>>>> 06534878862051449519ecf1deeb881859e3e735

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('nickname')
<<<<<<< HEAD
    return response
=======
    return response
>>>>>>> 06534878862051449519ecf1deeb881859e3e735
