from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from gallery.models import Gallery


class GalleryView(DetailView):
    model = Gallery
    template_name = "gallery/gallery.html"
    context_object_name = 'gallery'


class GalleryList(ListView):
	template_name = "gallery/gallery_list.html"
	model = Gallery

# Create your views here.
