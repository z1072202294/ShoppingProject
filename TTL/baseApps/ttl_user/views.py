from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect,QueryDict
from django.template import loader,RequestContext
from django.core.cache import cache
from django import forms
from .models import UserInfo
from . import smFunc



# from Demopycharm.My_first_django.淘乐乐.ShoppingProject.TTL.baseApps.ttl_user.utils import smFunc
# from TTL.baseApps.ttl_user.utils import smFunc



import inspect

def get__function_name():
    '''获取正在运行函数(或方法)名称'''
    return inspect.stack()[1][3]


REGIS_PAGES_HTML = "ttl_user/register.html"
USER_CENTER_HTML = 'ttl_user/center.html'
USER_INFO_HTML = "ttl_user/info.html"
USER_ORDER_HTML = "ttl_user/order.html"
USER_SHOU_HTML = "ttl_user/shou.html"
USER_MODIFY_HTML = "ttl_user/modify.html"
INFO = None


# Create your views here.


import json

class Shou(View):


    def get(self,request):
        print("===========get")
        if not smFunc.judgSession(request):
            return redirect(reverse('login'))

        res = UserInfo.objects.filter(nickname=request.session['name'])
        shou = json.loads(res[0].shou)
        print(shou)
        shouAd = {"info":shou}
        return render(request,USER_SHOU_HTML,context=shouAd)
        # return JsonResponse(data=shouAd,safe=False)

    def post(self,request):
        print("==========POST")
        res = UserInfo.objects.filter(nickname=request.session['name'])
        shou = res[0]
        print("库中已存在的")
        print(shou.shou)
        data = request.POST
        r1,dit = saveShouInfo(shou,data)
        if r1:
            data = {"info":dit}
            return JsonResponse(data=data,safe=False)
        print("www")
        return HttpResponse(request,False)

    def delete(self,request):
        '''
                            res0 = request.DELETE
        AttributeError    WSGIRequest' object has no attribute 'DELETE'
        '''
        print("delete")
        name = request.session["name"]
        delete = QueryDict(request.body)
        a = delete.get('di')
        i = int(a)-10
        result = smFunc.dele(name,i)
        if result:
            del result
            dit = {"result":"success"}
            return JsonResponse(data=dit,safe=False)
        dit = {"status":200,"result":"fail"}
        return JsonResponse(data=dit,safe=False)


def shouModify(request):
    if not smFunc.judgSession(request):
        return redirect(reverse('login'))

    elif request.method == "GET":
        name = request.session["name"]
        # put = QueryDict(request.body)
        mi = request.GET.get('mi')
        # mi = put.get("mi")
        i = int(mi) -10
        result = smFunc.modifyget(name,i)
        print("=======get",result)
        return render(request,USER_MODIFY_HTML,context=result)
    print("=====post")
    res = request.POST
    name = request.session["name"]
    dit = {
        "addr" : res.get('addr'),
        "shouname" : res.get('shouname'),
        "tel" : res.get('tel'),
        "flag": res.get("mi"),
    }

    mi = int(res.get("mi"))-10
    result = smFunc.modifypost(name,mi,dit)
    cont = {"result":result,"REDIRECT":reverse("shou")}
    return JsonResponse(data=cont,safe=False)




def saveShouInfo(shou,data):
    lst = json.loads(shou.shou)
    print("===========提取解=loads======>",lst)
    dit = {
        "addr":data['addr'],
        "shouname":data['shouname'],
        "tel":data['tel'],
        "flag":len(lst)+10
    }
    lst.append(dit)
    print("===append=======> ",lst)
    real_shou = json.dumps(lst)
    print("====dumps=======>",real_shou)
    shou.shou = real_shou
    shou.save()
    return True,dit

def backCenterInfo(obg):
    data = json.loads(obg.shou)
    length = len(data)
    if not len(data):
        shou_str = ""
    else:
        shou_str = data[length-1]["addr"][:8]+"    ...    "+str(len(data))+"条地址"
    dit = {
        "uName":obg.nickname,
        "phone":obg.phone,
        "email":obg.email,
        "shou":shou_str
    }
    return dit

class UserCenterView(View):
    '''
        Dispose Usercenter requests
    '''

    def get(self,request):
        if not smFunc.judgSession(request):
            return redirect(reverse('login'))

        elif UserInfo.objects.filter(nickname=request.session['name']):
            name = request.session['name']
            res = UserInfo.objects.filter(nickname=name)
            print(request.session["name"])
            print(res)
            res1 = res[0].shou
            print(json.loads(res1))
            dit = backCenterInfo(res[0])
            # return render(request,USER_CENTER_HTML)
            return render(request,USER_CENTER_HTML,context=dit)
        return redirect(reverse('login'))

    def post(self,request):

        print('=====post')


class RegisterView(View, smFunc.RegisOpera):
    '''
        dispose registerPages requests
    '''

    def get(self,request):

        content = {"REGIS":self.__class__.__name__}
        return render(request,REGIS_PAGES_HTML,context=content)

    def post(self,request):
        res = request.POST
        res1 = request.body
        back_v = self.disposePost(res)
        if back_v != self.REDIRECT:
            return JsonResponse(back_v, safe=False)

        back_v["redirect"] = reverse("login")
        print(back_v)
        return JsonResponse(back_v,safe=False)

def login(request):

    REDIRECT = {}
    FAIL = 0


    if request.method == 'POST':
        print("==============post")
        res = request.POST
        print(res)
        backv = smFunc.loginOpera(res)
        # cache.set("info", info,3600)
        if backv:
            print("=====登录成功")
            REDIRECT["redirect"] = reverse("index")
            url = request.COOKIES.get('url', '/')
            request.session["name"] = res['loginname']
            request.session["is_login"] = True
            red = HttpResponseRedirect(url)
            return red
        print("登录失败")
        request.session["is_login"] = False
        request.session["result"] = '1'
        red = HttpResponseRedirect("/user/login/")
        return (red)

    else:
        print("======================get")
        print(get__function_name())
        print(type(get__function_name()))
        content = {"LOGIN":get__function_name()}
        return render(request,REGIS_PAGES_HTML,context=content)





#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('nickname')

    return response


