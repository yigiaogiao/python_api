# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/18 11:57
from flask import current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import RedPrint
from app.models.user import User
from app.validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

api = RedPrint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify,
    }
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    # 生成token
    # 过期时间
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'],
                                form.type.data,
                                identity['scope'],
                                expiration)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """
    生成令牌需要在token中携带以下信息：
    ac_type 用户登录客户端的类型
    scope 权限控制
    expiration 过期时间
    """
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    # dumps方法加密token
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })

