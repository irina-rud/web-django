from gallery.models import Gallery

from django.shortcuts import get_object_or_404, resolve_url
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from gallery import models


class GalleryList(ListView):
    template_name = "gallery/gallery_list.html"
    model = Gallery
    context_object_name = 'galleries'

    # def dispatch(self, request, *args, **kwargs):
    #     self.form = GallerySearchSortForm(request.GET)
    #     self.form.is_valid()
    #     self.gallery_form = GalleryForm()
    #     return super(GalleryList, self).dispatch(request, *args, **kwargs)
    #
    # def get_queryset(self):
    #     queryset = Gallery.objects.all()
    #     if self.form.cleaned_data.get('search'):
    #         queryset = queryset.filter(title__icontains=self.form.cleaned_data.get('search'))
    #     if self.form.cleaned_data.get('sort_field'):
    #         queryset = queryset.order_by(self.form.cleaned_data.get('sort_field'))[:10]
    #     return queryset
    #
    # def get_context_data(self, **kwargs):
    #     context = super(GalleryList, self).get_context_data(**kwargs)
    #     context['form'] = self.form
    #     return context


class GalleryView(DetailView):
    model = Gallery
    template_name = 'gallery/gallery_detail.html'
    context_object_name = 'gallery'


class GalleryDetail(CreateView):
    model = Gallery
    template_name = 'gallery/gallery_detail.html'
    context_object_name = 'gallery'
    fields = ('title')

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.gallery = get_object_or_404(Gallery.objects.all(), pk=pk)
        return super(GalleryDetail, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(GalleryDetail, self).form_valid(form)

    def get_success_url(self):
        return resolve_url("galleries:gallery_detail", pk=self.gallery.pk)

    def get_context_data(self, **kwargs):
        context = super(GalleryDetail, self).get_context_data(**kwargs)
        context['gallery'] = self.gallery
        return context


class GalleryCreate(CreateView):
    model = models.Gallery
    template_name = 'gallery/new.html'
    fields = ('title',)
    context_object_name = 'gallery'

    def get_success_url(self):
        return resolve_url('galleries:gallery_detail', pk=self.object.pk)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(GalleryCreate, self).form_valid(form)


class GalleryUpdate(UpdateView):
    template_name = 'gallery/gallery_update.html'
    model = Gallery
    fields = ('title',)
    context_object_name = 'gallery'

    def get_queryset(self):
        return super(GalleryUpdate, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return resolve_url('galleries:gallery_update', pk=self.object.pk)
