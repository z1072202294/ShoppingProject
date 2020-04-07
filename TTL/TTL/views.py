from django.shortcuts import render,redirect,reverse
from django.views import View
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from django import forms

def index(request):
    return render(request,'index.html')