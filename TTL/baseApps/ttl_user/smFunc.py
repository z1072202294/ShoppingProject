# from Demopycharm.My_first_django.淘乐乐.ShoppingProject.TTL.baseApps.ttl_user.models import UserInfo
# from ..models import UserInfo
from .models import UserInfo
from .models import UserInfo
import json
import hashlib


def encryptionMd5(res):
    md5 = hashlib.md5()
    md5.update(res.encode('utf8'))
    return md5.hexdigest()

def encryptionSha1(res):
    sha1 = hashlib.sha1('abc'.encode('utf8'))
    return sha1.hexdigest()

def de_savePwd(f):
    def inner(dict1):
        username,email,phone,pwd1= f(dict1)
        real_pwd = encryptionSha1(pwd1)
        user = UserInfo.objects.create(nickname=username, password=real_pwd,email=email,phone=phone)
        user.save()
    return inner

@de_savePwd
def savePwd(dict1):
    print(dict1)
    return dict1['nickname'],dict1['email'],dict1['tel'],dict1['pwd']




class RegisOpera():

    SUCCESS_RESULT = {"result": 1}
    FAIL_RESULT = {"result": 0}
    REDIRECT = {}


    @classmethod
    def decode_loads(cls,backData,entp='utf8'):
        res = backData.decode(entp)
        return json.loads(res)

    @classmethod
    def disposePost(cls,dict1):
        """
        判断 Register Post
        """

        if "judgUsname" in dict1.keys():
            print("判断name")
            #  Judg username
            if UserInfo.objects.filter(nickname=dict1['judgUsname']).exists():
                print("存在")
                print(dict1["judgUsname"])
                return cls.FAIL_RESULT
            else:
                print("不存在")
                print(dict1["judgUsname"])
                return cls.SUCCESS_RESULT

        else:
            # save pwd
            print("保存密码")
            savePwd(dict1)
            return cls.REDIRECT





def loginOpera(dict):

    back_t = {}
    name = dict['nickname']
    pwd = dict['pwd']
    usr = UserInfo.objects.filter(nickname=name).exists()
    if usr:
        quObg = UserInfo.objects.filter(nickname=name)
        realPwd = quObg[0].password
        pwd = encryptionSha1(pwd)
        if pwd == realPwd:
            print()
            return True
        else:
            return False
    else:
        return False
