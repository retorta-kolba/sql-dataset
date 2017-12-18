from data import views
from django.conf.urls import url

urlpatterns = [
    url(r'^aa$', views.test , name='account'),
    url(r'^datasets/$', views.datasets , name='datasets'),
    url(r'^datasources/$', views.datasources , name='datasources'),
    url(r'^sciencefields/$', views.sciencefields , name='sciencefields'),
    url(r'^dataset/(?P<id>\d+)$', views.dataset , name='dataset'),
    url(r'^dataset/(?P<id>\d+)/edit$', views.newdataset , name='dataset'),
    url(r'^dataset/new$', views.newdataset, name='newdataset'),
    url(r'^datasource/(?P<id>\d+)$', views.datasource , name='datasource'),
    url(r'^sciencefield/(?P<id>\d+)$', views.sciencefield , name='sciencefield'),
    url(r'^authors/$', views.authors , name='authors'),
    url(r'^author/(?P<id>\d+)$', views.author , name='author'),
    url(r'^search', views.search, name='search'),
    url(r'^author/(?P<id>\d+)/edit$', views.newauthor , name='dataset'),
    url(r'^author/new$', views.newauthor, name='newdataset'),
    url(r'^$', views.index, name='index'),
    url(r'^sciencefield/new$', views.newsciencefield, name='newdataset'),
    url(r'^datasource/new$', views.newdatasource, name='newdataset'),
    url(r'^sciencefield/(?P<id>\d+)/edit$', views.newsciencefield , name='dataset'),
    url(r'^datasource/(?P<id>\d+)/edit$', views.newdatasource , name='dataset'),
]