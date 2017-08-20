from django.conf.urls import url
from . import views


# Our urlpatterns to be examined when django is redirected from djangogirls.urls

urlpatterns = [

	# Only an empty string will match
	# In django URL resolvers, 'http:127.0.0.1:8000/' is not a part of URL
	# This pattern will tell django that 'views.post.list' is the right place
	# When someone visits 'http:127.0.0.1:8000/' 
	# name='post_list' is the name used to identify the url used to identify view
	url(r'^sys_info_page$', views.sys_info_page, name='sys_info_page'),
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]