from django.shortcuts import render
from django.views import View
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from django import forms
from .models import UserInfo

# from Demopycharm.My_first_django.淘乐乐.ShoppingProject.TTL.baseApps.ttl_user.utils import smFunc

# from TTL.baseApps.ttl_user.utils import smFunc

from ttl_user import smFunc

# Create your views here.

class RegisterView(View, smFunc.User_opera):
    '''
        dispose registerPages requests
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



#表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())


#登陆
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            nickname = uf.cleaned_data['nickname']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = UserInfo.objects.filter(username__exact = nickname,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/user/register/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('nickname',nickname,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/user/login/')
    else:
        uf = UserForm()
        return render('/ttl_user/login.html',{'uf':uf})

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