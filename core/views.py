from comment.models import Comment
from django.views.generic import TemplateView

from gallery.models import Gallery
from post.models import Post


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['last_posts'] = Post.objects.filter(is_published=True)[:5]
        context['last_comments'] = Comment.objects.filter(post__is_published=True)[:5]
        context['galleries'] = Gallery.objects.all()
        return context
