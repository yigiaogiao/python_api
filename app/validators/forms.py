# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/14 10:59
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
    # 账号
    account = StringField(validators=[DataRequired(message='不允许为空'), length(
        min=5, max=32
    )])
    # 密码
    secret = StringField()
    #  客户端类型
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        """
        自定义type验证器
        :param value: 将传递过来的数字转换为枚举,再将枚举赋值给type
        :return:
        """
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()
