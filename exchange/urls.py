from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from exchange.views import signup, december, upload_sketch

urlpatterns = [
    url(r'^$', signup, name='signup'),
    url(r'^december/$', december, name='december'),
    url(r'^upload/(?P<assignment_pk>\d+)/(?P<tag>\w+)/(?P<password>\w+)/$', upload_sketch, name='upload_sketch'),
]