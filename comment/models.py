# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Comment(models.Model):
    text = models.TextField(verbose_name=u'Текст комменария')
    post = models.ForeignKey('post.Post')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор')

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        ordering = ('-created_at',)

    def __unicode__(self):
        return self.text
