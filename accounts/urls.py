from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^login/$', views.login, name='login'),
	url(r'^(?P<ID>[0-9]+)/$', views.user, name='accounts-user'),
	url(r'^settings/$', views.settings, name='accounts-settings'),
	url(r'^$', views.users, name='accounts-users'),
)
