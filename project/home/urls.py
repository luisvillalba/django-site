from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
