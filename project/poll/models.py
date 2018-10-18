# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    person_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Poll(models.Model):
    poll_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vote(models.Model):
    poll_id = models.ForeignKey(Poll)
    person_id = models.ForeignKey(Person)
    vote_id = models.IntegerField(unique=True)
    value = models.CharField(max_length=10)

    def __str__(self):
        return str(self.vote_id)

