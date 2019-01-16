#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 16:06
# @Author  : Aries
# @Site    : 
# @File    : urls.py
# @Software: PyCharm2018.2
from django.urls import path,re_path
from .views import index, show

urlpatterns = [
    path('index/', index),
    re_path(r'index/(\d+)$', show)
]


