from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^list/(\d+)_(\d+)_(\d+)$', views.list),
    url(r'^(\d+)/$', views.detail),
    url(r'^demo/$', views.demo),
    url(r'^search/', views.MySearchView.as_view()),
]