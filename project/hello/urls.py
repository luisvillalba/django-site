from django.conf.urls import url
from hello import views

urlpatterns = [
    url(r'^say_hello', views.index, name="index"),
    url(r'^help', views.help, name="help"),
]
