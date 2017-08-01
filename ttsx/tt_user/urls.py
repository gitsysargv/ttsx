from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^handle/$', views.handle),
    url(r'^reuse/$', views.reuse),
]