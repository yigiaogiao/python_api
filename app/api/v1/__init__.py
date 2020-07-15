# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/13 10:48
from flask import Blueprint
from app.api.v1 import user, book, clients


def create_bkueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1, url_prefix='/user')
    book.api.register(bp_v1, url_prefix='/book')
    clients.api.register(bp_v1)
    return bp_v1
