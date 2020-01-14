from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from exchange.views import signup, december, upload_sketch, review, review_sketches, rematch_guide

urlpatterns = [
    url(r'^$', signup, name='signup'),
    url(r'^december/$', december, name='december'),
    url(r'^upload/(?P<assignment_pk>\d+)/(?P<tag>\w+)/(?P<password>\w+)/$', upload_sketch, name='upload_sketch'),
    url(r'^review/(?P<exchange>\w+)/(?P<assignment_pk>\d+)/(?P<tag>\w+)/(?P<password>\w+)/$', review_sketches, name='review'),
    url(r'^review/(?P<exchange>\w+)/$', review, name='review'),
    url(r'^rematch_guide/(?P<exchange>\w+)/$', rematch_guide, name='rematch_guide'),
    # url(r'^review/', review, name='review'),
]