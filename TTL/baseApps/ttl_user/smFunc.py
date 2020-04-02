# from Demopycharm.My_first_django.淘乐乐.ShoppingProject.TTL.baseApps.ttl_user.models import UserInfo
from .models import UserInfo

# from ..models import UserInfo


import json

class User_opera():

    field_lst = ['nickname']

    @classmethod
    def decode_loads(cls,backData,entp='utf8'):
        res = backData.decode(entp)
        return json.loads(res)

    @classmethod
    def judgAuth(cls,nickname,password,email,show,youbian,phone):

        if not UserInfo.objects.filter(nickname=nickname).exists():
            return "用户名已存在!"
        else:
            user = UserInfo.objects.create(nickname=nickname,password=password,email=email,shou=show,youbian=youbian,phone=phone)
            user.save()
            return "注册成功"
