from django.conf.urls import url
from . import views
# this is the list of urls for the app
urlpatterns=[
    url(r'^reset$', views.reset),
    url(r'^submit$', views.submit),
    url(r'^', views.index),
]
