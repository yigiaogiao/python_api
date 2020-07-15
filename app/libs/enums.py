# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/14 10:54
from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101
    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
