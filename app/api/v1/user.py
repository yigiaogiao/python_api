# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/13 10:48
from flask import jsonify, g

from app.libs.error_code import DeleteSuccess
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = RedPrint('user')


# 超级管理员查看所有账号
@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


# 普通用户查看自己账号
@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.id
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


# 超级管理员删除所有账号
@api.route('/<int:uid>', methods=['DELETE'])
def super_delete_user(uid):
    pass


# 普通用户删除自己账号
@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    # 哪怕同一时刻有两个用户访问g变量也不会出现数据混淆，g变量时线程隔离的
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        # 调用的base基类下的方法软删除
        user.delete()
    return DeleteSuccess()

