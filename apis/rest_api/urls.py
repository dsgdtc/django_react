#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: urls.py
Author: guyu
Date: 2017/6/12 19:55
"""

from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers

from apis.rest_api import views

#debug_router = routers.DefaultRouter()
#debug_router.register(r'debug', views.BasedClassView, base_name='debug')

urlpatterns = [
    url(r'^debug/', views.ClassBasedView.as_view(), name='debug'),
]
