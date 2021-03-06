from django.conf.urls import url

from news import views

urlpatterns = [
	url(r'^add/$', views.add, name='news-add'),
	url(r'^edit/(?P<ID>[0-9]+)/$', views.edit, name='news-edit'),
	url(r'^(?P<page>[0-9]+)/$', views.news, name='news-news'),
	url(r'^$', views.news, name='news-news'),
]
