# from Demopycharm.My_first_django.淘乐乐.ShoppingProject.TTL.baseApps.ttl_user.models import UserInfo
# from ..models import UserInfo
from ttl_user.models import UserInfo
import json
import hashlib


def encryption(res):
    md5 = hashlib.md5()
    md5.update(res.encode('utf8'))
    return md5.hexdigest()


def de_savePwd(f):
    def inner(dict1):
        username,email, show,youbian,phone,pwd1= f(dict1)
        real_pwd = encryption(pwd1)
        print(real_pwd)
        user = UserInfo.objects.create(nickname=username, password=real_pwd,email=email, shou=show, youbian=youbian,phone=phone)
        user.save()
    return inner


@de_savePwd
def savePwd(dict1):
    return dict1['nickname'],dict1['email'],dict1['shou'],dict1['youbian'],dict1['phone'],dict1['password1']

class User_opera():


    @classmethod
    def decode_loads(cls,backData,entp='utf8'):
        res = backData.decode(entp)
        return json.loads(res)

    @classmethod
    def judgAuth(cls,dict1):
        print('判断注册')
        if UserInfo.objects.filter(nickname=dict1['nickname']).exists():
            return "用户名已存在!"

        else:
            savePwd(dict1)
            return "注册成功"
