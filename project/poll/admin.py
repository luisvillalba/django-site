# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from poll.models import Person, Vote, Poll

admin.site.register(Person)
admin.site.register(Vote)
admin.site.register(Poll)


# Register your models here.
