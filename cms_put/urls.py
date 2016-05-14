from django.conf.urls import url
from . import views

app_name = 'cms_put'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'(?P<nombre>.*)$', views.recurso, name="recurso"),
]