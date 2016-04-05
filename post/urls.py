from django.conf.urls import url

import post
from .views import *

urlpatterns = [
	url(r'^posts/$', PostList.as_view(), name="post_list"),
	url(r'^(?P<pk>\d+)/$', PostView.as_view(), name="post_detail"),
	url(r'^search-form/$', post.views.search_form, name="search_form"),
	url(r'^new/$', post.views.PostCreate.as_view(), name='create'),

]
