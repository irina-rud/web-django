from django.conf.urls import url
from django.contrib.auth.decorators import login_required

import post.views

urlpatterns = [
    url(r'^posts/$', post.views.PostList.as_view(), name="post_list"),
    url(r'^(?P<pk>\d+)/$', post.views.PostDetail.as_view(), name="post_detail"),
    url(r'^search-form/$', post.views.search_form, name="search_form"),
    url(r'^new/$', login_required(post.views.PostCreate.as_view()), name='post_create'),
    url(r'^(?P<pk>\d+)/update/$', post.views.PostUpdate.as_view(), name='post_update'),
    url(r'^(?P<pk>\d+)/ajax/$', post.views.PostCommentsAjax.as_view(), name='post_comments'),
]
