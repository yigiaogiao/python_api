# -*-coding:utf-8-*-
# author: xdz
# @Time :2020/7/13 10:03
from app.app import create_app

app = create_app()





if __name__ == '__main__':
    app.run(debug=True)