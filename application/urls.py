"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.contrib.auth.views import login, logout

import post
from gallery.views import GalleryList
from post.views import PostList

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^post/', include('post.urls', namespace="post")),
    url(r'^posts/$', PostList.as_view(), name="post_list"),
    url(r'^gallery/', include('gallery.urls', namespace="gallery")),
    url(r'^galleries/$', GalleryList.as_view(), name="gallery_list"),
    url(r'^login/', login, {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/', logout, {'template_name': 'core/logout.html'}, name="logout"),
    #url(r'^search-form/', 'post.views.search_form'),
    url(r'^$', PostList.as_view(), name="post_list"),
    url(r'^new/', post.views.PostCreate.as_view()),
]