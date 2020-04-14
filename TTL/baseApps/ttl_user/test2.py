import django
import os,sys,requests,json


# os.environ['DJANGO_SETTINGS_MODULE'] = 'TTL.settings'
# django.setup()

# from django.core.cache import cache



# def w():
#     cache['name'] = "chqbg"
#     return

import hashlib

string="rootroot"
sha1 = hashlib.sha1()
sha1.update(string.encode('utf-8'))
res = sha1.hexdigest()
print("sha1加密结果:",res)

# 7b21848ac9af35be0ddb2d6b9fc3851934db8420
