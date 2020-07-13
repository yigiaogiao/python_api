# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/13 10:48
from flask import Blueprint

from app.libs.redprint import RedPrint

api = RedPrint('book')

@api.route('/get')
def get_book():
    return 'book get'

@api.route('/create')
def create_book():
    return 'create book'