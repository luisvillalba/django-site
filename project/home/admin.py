# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from home.models import AuthorModel

# Re-register UserAdmin
admin.site.register(AuthorModel)
