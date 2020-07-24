# -*-coding:utf-8-*- 
# author: xdz
# @Time :2020/7/22 10:29

class QiYue:
    name = 'qiyue'
    age = 18

    def __init__(self):
        self.gender = 'male'

    def keys(self):
        return ('name','age','gender')

    def __getitem__(self, item):
        return getattr(self, item)


o = QiYue()
print(dict(o))