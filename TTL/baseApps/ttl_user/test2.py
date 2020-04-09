import django
import os,sys,requests,json


os.environ['DJANGO_SETTINGS_MODULE'] = 'TTL.settings'
django.setup()

from django.core.cache import cache



def w():
    cache['name'] = "chqbg"
    return

