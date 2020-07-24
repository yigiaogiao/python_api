# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/24 11:13


class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    # 运算符重载
    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        # 集合set默认去重
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        # 集合set默认去重
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        # 集合set默认去重
        self.forbidden = list(set(self.forbidden))
        return self


class AdminScope(Scope):
    # allow_api = ['v1.user+super_get_user', 'v1.user+super_delete_user']
    allow_module = ['v1.user']

    def __init__(self):
        pass


class UserScope(Scope):
    forbidden = ['v1.user+super_get_user', 'v1.user+super_delete_user']

    def __init__(self):
        self + AdminScope()


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    # 判断传递进来的endpoint是否在可以访问的权限类的属性中
    # 默认的endpoint是v1.super_get_user 我们自定义为v1.moduke_name(模块名)+super_get_user
    # v1.redpint
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False
