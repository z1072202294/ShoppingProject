from django.shortcuts import render,redirect,reverse
from django.views import View
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from django import forms


def index(request):
    if request.method == "POST":
        print("post == 首页   ")
        res = request.POST
        return render(request,'index.html',context=res)

    else:
        print("get == 首页 ")
        if request.session.get("is_login"):
            print(request.session["name"])
            return render(request,"index.html")
        print("没有登陆session")
        return render(request,'index.html')
