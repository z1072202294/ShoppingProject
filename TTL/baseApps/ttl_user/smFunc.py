
# from Demopycharm.My_first_django.淘乐乐.ShoppingProject.TTL.baseApps.ttl_user.models import UserInfo
# from ..models import UserInfo

from django.core.cache import cache
from .models import UserInfo
from .models import UserInfo
import json
import hashlib



def encryptionMd5(res):
    md5 = hashlib.md5()
    md5.update(res.encode('utf8'))
    return md5.hexdigest()

def encryptionSha1(res):
    sha1 = hashlib.sha1(res.encode('utf8'))
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
                print("已有name存在")
                print(dict1["judgUsname"])
                return cls.FAIL_RESULT
            else:
                print("name不存在可注册")
                print(dict1["judgUsname"])
                return cls.SUCCESS_RESULT

        else:
            # save pwd
            print("保存密码")
            savePwd(dict1)
            print(UserInfo.objects.filter(nickname=dict1['nickname']))
            return cls.REDIRECT


def judgSession(request):
    is_login = False
    if request.session.get('is_login'):
        is_login = True
    return is_login

def updatUser(id,data):
    user = UserInfo.objects.filter(id=id)[0]
    print(user)
    judg = data["judg"]
    val = data["val"]
    try:
        if judg == "1":
            user.nickname=val
        elif judg == "2":
            user.phone=val
        elif judg == "3":
            user.email=val
        user.save()
        return 1
    except:
        return 0

def loginOpera(dict):

    name = dict.get('loginname')
    pwd = dict.get('loginpwd')
    print(name,"==")
    print(pwd,"==")
    usr = UserInfo.objects.filter(nickname=name).exists()
    print("user==",usr)
    if usr:
        print("操作data")
        quObg = UserInfo.objects.filter(nickname=name)
        print("取出比较")
        realPwd = quObg[0].password
        pwd = encryptionSha1(pwd)
        if pwd == realPwd:
            print("相等")
            return True
        else:
            return False
    else:
        return False


def dele(user_id,i):
    u1 = UserInfo.objects.filter(id=user_id)[0]
    print(u1)
    print("============delete",type(u1.shou))
    shou1 = json.loads(u1.shou)
    del shou1[i]
    u1.shou = json.dumps(shou1)
    u1.save()
    return True


def modifyget(user_id,i):
    u1 = UserInfo.objects.filter(id=user_id)[0]

    shou1 = json.loads(u1.shou)
    result = {"info":shou1[i]}
    return result

def modifypost(user_id,i,dict):
    try:
        u1 = UserInfo.objects.filter(id=user_id)[0]
        shou1 = json.loads(u1.shou)
        shou1[i] = dict
        u1.shou = json.dumps(shou1)
        u1.save()
        return 1
    except:
        return 0




