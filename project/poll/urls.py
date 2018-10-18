from django.conf.urls import url
from poll import views

urlpatterns = [
    url(r'^votes', views.votes, name="votes"),
    url(r'^form', views.form, name="form")
]
