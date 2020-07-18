# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/15 13:21
from werkzeug.exceptions import HTTPException

from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class ClientTpyeError(APIException):
    # 400 请求参数错误 401 未授权 403 禁止访问 404 没有找到资源
    # 500 服务器产生未知错误
    # 200 查询成功 201 创建更新成功 204 删除成功
    # 301 302 重定向
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000
