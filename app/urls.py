from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.default, name='default'),
    url(r'^catalog$', views.catalog, name='catalog'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^download/(?P<filename>[\w\W]+)$', views.download, name='download'),
    url(r'^remove/(?P<filename>[\w\W]+)$', views.remove, name='remove')
]