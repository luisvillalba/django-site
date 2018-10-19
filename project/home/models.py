# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager


class AuthorModel(AbstractBaseUser):
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    objects = UserManager()


class PostModel(models.Model):
    heading = models.CharField(max_length=400)
    text = models.CharField(max_length=50000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

