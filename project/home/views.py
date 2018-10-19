# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

app_name = 'home'

# Create your views here.
def index(request):
    return render(request, 'home/index.html')
