from django.test import TestCase
import django
import os,sys,requests,json

os.environ['DJANGO_SETTINGS_MODULE'] = 'TTL.TTL.settings'
django.setup()

# Create your tests here.
url = 'http://127.0.0.1:8000/user/register/'

print(sys.path)

d1 = {'11':22}
data = json.dumps(d1)
print(data)
# res = requests.post(url=url,data=data)
# res.encoding = 'utf8'
# print(res.text)



# from TTL.baseApps.ttl_user.models import UserInfo
from .models import UserInfo



dict1 = {
    'nickname':'名称',
    'password':'密码',
    'email' : '1149603874@',
    'shou':'收货地址',
    'youbian':'邮政编码',
    'phone':'15935341565'
}



print(UserInfo.__doc__)
# u1 = UserInfo.objects.create(nickname='名称',password='密码',email='1149603874@qq.com',shou='收获地址',youbian='邮政编码',phone='15935341565')
# u1.save()

# print(UserInfo.objects.all().exists())
# print(UserInfo.objects.filter(nickname='www').exists())

