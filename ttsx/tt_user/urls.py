from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^handle/$', views.handle),
    url(r'^reuse/$', views.reuse),
    url(r'^$', views.user_center_info),
    url(r'^login_handle/$', views.login_handle),
    url(r'^user_center_order/$', views.user_center_order),
    url(r'^site/$', views.site),
]