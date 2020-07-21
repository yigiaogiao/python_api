# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/13 10:48
from app.libs.error_code import NotFound
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.user import User

api = RedPrint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)

    return user