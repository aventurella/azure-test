from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r"^$", "azure.views.action", name="home"),
    url(r"^foo/", "azure.views.foo", name="foo"),
)
