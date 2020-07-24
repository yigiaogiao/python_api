# -*-coding:utf-8-*-
# author: xdz
# @Time :2020/7/13 10:03
from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    """
    继承异常基类Exception，flask最底层的异常类
    """
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式
        # log
        # 判断如果属于debug是true那么else返回详细报错信息，否则返回我们特定的json
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
