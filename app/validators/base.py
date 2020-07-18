# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/16 15:13
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        data = request.json
        # 如果是json格式的数据传递到wtform中需要data=，表单提交的直接传入data
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        """
        判断完成以后将报错的list通过异常类构建成json数据返回给前端
        """
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
