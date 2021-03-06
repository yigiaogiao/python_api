# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/14 10:40
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTpyeError, Success
from app.libs.redprint import RedPrint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = RedPrint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {ClientTypeEnum.USER_EMAIL: __register_user_by_email}
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    """
    用户通过email注册,验证email方式传递的数据
    """
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,
                           form.account.data, form.secret.data)
