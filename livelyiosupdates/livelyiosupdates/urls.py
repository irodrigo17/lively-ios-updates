from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^iPhone$', 'myapp.views.index'),
)
