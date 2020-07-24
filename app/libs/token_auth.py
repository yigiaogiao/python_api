# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/21 9:11
from collections import namedtuple

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import is_in_scope

auth = HTTPBasicAuth()
User = namedtuple('User', {'uid', 'ac_type', 'scope'})


@auth.verify_password
def verify_password(token, password):
    """
    account:账号（实际传入的是token的值）
    password: 密码
    验证token的合法性
    """
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    # BadSignature验证token是否合法
    except BadSignature:
        raise AuthFailed(msg='token is invalid',
                         error_code=1002)
    # SignatureExpired验证token是否过期
    except SignatureExpired:
        raise AuthFailed(msg='token is expired',
                         error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    scope = data['scope']
    # 这里还可以获取request需要访问哪个接口
    allow = is_in_scope(scope, request.endpoint)
    if not allow:
        raise Forbidden
    return User(uid, ac_type, scope)
