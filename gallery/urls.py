from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^galleries/$', GalleryList.as_view(), name="gallery_list"),
	url(r'^(?P<pk>\d+)/$', GalleryView.as_view(), name="gallery_detail"),
]
