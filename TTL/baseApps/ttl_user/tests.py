from django.test import TestCase
import django
import os,sys,requests,json

os.environ['DJANGO_SETTINGS_MODULE'] = 'TTL.TTL.settings'
django.setup()

# from TTL.baseApps.ttl_user.models import UserInfo
from ttl_user.models import UserInfo
# print(sys.path)


'''
=====================================================
'''



# Create your tests here.
url = 'http://127.0.0.1:8000/user/register/'



dict1 = {
    'nickname':'名',
    'password1':'密码',
    'password2':'密码',
    'email' : '1149603874@qq.com',
    'shou':'收获地址',
    'youbian':'邮政编码',
    'phone':'15935341565'
}
d1 = {'11':22}
data = json.dumps(dict1)
print(data)
res = requests.post(url=url,data=data)
res.encoding = 'utf8'
print(res.text)
# print(json.loads(res.text))




#
# if not False:
#     print(1)
# else:
#     print(2)

# print(UserInfo.__doc__)
# u1 = UserInfo.objects.create(nickname='名称',password='密码',email='1149603874@qq.com',shou='收获地址',youbian='邮政编码',phone='15935341565')
# u1.save()

# print(UserInfo.objects.all().exists())
# print(UserInfo.objects.filter(nickname='www').exists())

import hashlib
def encryption(res):
    md5 = hashlib.md5()
    md5.update(res.encode('utf8'))
    return md5.hexdigest()



# def de(f):
#     def inner(x,y):
#         if x == '1':
#             res =  '1'
#         else:
#             res = encryption(res=x)
#         f(res,y)
#         print('后置')
#     return inner
#
#
# @de
# def pri(x):
#     return x
#
# pri('1')

def de_savePwd(f):
    def inner(instance,food):
        res = f(instance,food)
        print('后置')
    return inner


class A():

    @de_savePwd
    def good(self,*args):
        print(*args)
        return args

    @classmethod
    def main(cls,food='fish'):
        cls.good(food)

#
# a = A()
#
# a.main()
