from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^home_page.html', views.index, name = 'about'),
	url(r'^load/', views.load, name = 'load'),
	url(r'^get_usernames/', views.get_usernames, name = 'get_usernames'),
	url(r'^report/', views.report, name = 'report'),
	url(r'^flag/', views.flag, name = 'flag'),
	url(r'^color/', views.color, name = 'color'),
	#url(r'^something', views.base, name = 'base,')
]