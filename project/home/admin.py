# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from home.models import AuthorModel

class AuthorInline(admin.StackedInline):
    model = AuthorModel
    can_delete = False
    verbose_name_plural = 'author'

class UserAdmin(BaseUserAdmin):
    inlines = (AuthorInline,)

# Re-register UserAdmin
admin.site.register(User, UserAdmin)
