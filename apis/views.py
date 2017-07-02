#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render,HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
# import os,sys
# sys.path.append(os.path.dirname(__file__))
from rest_framework.views import APIView
from rest_framework import viewsets
from django.conf import settings


def react(request):
    SERVER_ADDR = settings.SERVER_ADDR
    return render_to_response('react/index.html',locals())
