from data import views
from django.conf.urls import url

urlpatterns = [
    url(r'^aa$', views.test , name='account'),
    url(r'^datasets/$', views.datasets , name='datasets'),
    url(r'^dataset/(?P<id>\d+)$', views.dataset , name='dataset'),
]