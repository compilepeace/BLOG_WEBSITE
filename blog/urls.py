from django.conf.urls import url
from . import views


# Our urlpatterns to be examined when django is redirected from djangogirls.urls

urlpatterns = [

	# Only an empty string will match
	# In django URL resolvers, 'http:127.0.0.1:8000/' is not a part of URL
	# This pattern will tell django that 'views.post.list' is the right place
	# When someone visits 'http:127.0.0.1:8000/' 
	# name='post_list' is the name used to identify the url used to identify view
	url(r'^$', views.sys_info_page, name='sys_info_page'),
	url(r'^post$', views.post_list, name='post_list'),

]