from django.core.urlresolvers import reverse
from django.forms import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, resolve_url
from django.template import context
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

import post
from post import models
from post.forms import SearchForm, PostForm, PostSearchSortForm
from .models import Post

class PostList(ListView):

    template_name = "post/post_list.html"
    model = Post
    context_object_name = 'posts'

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
        context['form'] = self.form
        return context


class PostView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
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


class PostDetail(CreateView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'
    fields = ('title', 'sign', 'picture')
    context_object_name = 'comment'

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.post = get_object_or_404(Post.objects.all(), pk=pk)
        return super(PostDetail, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.post = self.post
        form.instance.author = self.request.user
        return super(PostDetail, self).form_valid(form)

    def get_success_url(self):
        return resolve_url("posts:post_detail", pk=self.post.pk)

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['post'] = self.post
        return context


class PostCreate(CreateView):
    model = models.Post
    template_name = 'post/new.html'
    fields = ('title', 'sign', 'picture', 'is_published', 'gallery')
    context_object_name = 'post'

    def get_success_url(self):
        return resolve_url('posts:post_detail', pk=self.object.pk)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)


class PostUpdate(UpdateView):

    template_name = 'post/post_update.html'
    model = Post
    fields = ('title', 'sign', 'picture', 'is_published', 'gallery')
    context_object_name = 'post'

    def get_queryset(self):
        return super(PostUpdate, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return resolve_url('posts:post_update', pk=self.object.pk)


class PostCommentsAjax(DetailView):

    template_name = 'post/post_comments_ajax.html'
    model = Post
    context_object_name = 'post'
