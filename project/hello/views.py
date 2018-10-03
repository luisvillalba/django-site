# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    data = {'text': 'This is a template tag'}
    return render(request, 'hello/index.html', context=data)

def help(request):
    data = {'text': 'Hello, welcome to help'}
    return render(request, 'hello/help.html', context=data)
