from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from .models import UserInfo

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
            user = UserInfo.objects.filter(nickname = nickname,password = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/register/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('nickname',nickname,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/user/')
    else:
        uf = UserForm()
    return render('log.html',{'uf':uf})

#登陆成功
def index(req):
    username = req.COOKIES.get('nickname','')
    return render('index.html' ,{'nickname':username})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('nickname')
    return response
