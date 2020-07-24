# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/13 10:08


from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError
from datetime import date


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        # 判断对象o中是否含有keys或者__getitem__
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        else:
            raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder



