#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 9:28
# @Author  : Aries
# @Site    : 
# @File    : urls.py
# @Software: PyCharm2018.2
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index)
]
