from django.core.urlresolvers import reverse
from django.forms import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import context
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

import post
from post import models
from post.forms import SearchForm, PostForm
from .models import Post


class PostList(ListView):
    template_name = "post/post_list.html"
    model = Post


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
        return reverse('core:posts:post', args=[self.pk])

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)
