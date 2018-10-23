# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class AuthorModel(models.Model):
    user = models.OneToOneField(User)

    picture = models.ImageField(upload_to='profile_pics',blank=True)
    instagram = models.URLField(blank=True)
    
    def __str__():
        return self.user.username


class PostModel(models.Model):
    heading = models.CharField(max_length=400)
    text = models.CharField(max_length=50000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

