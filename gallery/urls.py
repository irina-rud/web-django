from django.conf.urls import url
from django.contrib.auth.decorators import login_required

import gallery
from .views import *

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', GalleryDetail.as_view(), name="gallery_detail"),
    url(r'^$', gallery.views.GalleryList.as_view(), name='gallery_list'),
    url(r'^create/$', login_required(gallery.views.GalleryCreate.as_view()), name='gallery_create'),
    url(r'^(?P<pk>\d+)/$', gallery.views.GalleryDetail.as_view(), name='gallery_detail'),
    url(r'^(?P<pk>\d+)/update/$', gallery.views.GalleryUpdate.as_view(), name='gallery_update'),
]
