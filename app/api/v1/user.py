# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/13 10:48
from flask import Blueprint

from app.libs.redprint import RedPrint


api = RedPrint('user')

@api.route('/get')
def get_user():
    return 'user get'