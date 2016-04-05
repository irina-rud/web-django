from django.core.urlresolvers import reverse
from django.forms import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, resolve_url
from django.template import context
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

import post
from post import models
from post.forms import SearchForm, PostForm, PostSearchSortForm
from .models import Post


class PostList(ListView):

    template_name = "post/post_list.html"
    model = Post

    def dispatch(self, request, *args, **kwargs):
        self.form = PostSearchSortForm(request.GET)
        self.form.is_valid()
        self.post_form = PostForm()
        return super(PostList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Post.objects.all()
        if self.form.cleaned_data.get('search'):
            queryset = queryset.filter(title__icontains=self.form.cleaned_data.get('search'))
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data.get('sort_field'))[:10]
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['form']= self.form
        return context


class PostView(DetailView):
    model = Post
    template_name = 'post/post.html'
    context_object_name = 'post'


def search_form(request):
    res = None
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            res = Post.objects.filter(sign=form.cleaned_data['query'])
    else:
        form = SearchForm()
    return render(request, 'search-form.html', {'form': form, 'res': res})


class PostDetails(object):
    model = Post
    template_name = 'post/new.html'

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.Post = get_object_or_404(Post, id=pk)
        return super(PostDetails, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        cntext = super(PostDetails, self).get_context_data(**kwargs)
        context['event'] = self.event
        return context


class PostCreate(CreateView):
    model = models.Post
    template_name = 'post/new.html'
    fields = ('title', 'sign', 'picture', 'is_published', 'gallery')

    def get_success_url(self):
        return resolve_url('posts:post_detail', pk=self.object.pk)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)
