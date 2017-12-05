from data import views
from django.conf.urls import url

urlpatterns = [
    url(r'^aa$', views.test , name='account'),
]