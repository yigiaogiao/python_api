# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/13 10:08
from flask import Flask


def register_blueprints(app):
    from app.api.v1 import create_bkueprint_v1
    app.register_blueprint(create_bkueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    return app
