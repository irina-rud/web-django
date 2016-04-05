# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    sign = models.CharField(max_length=31, verbose_name=u'Подпись')
    picture = models.ImageField(verbose_name=u'Картина')
    is_published = models.BooleanField(default=False, verbose_name=u'Было ли опубликовано')
    gallery = models.ForeignKey('gallery.Gallery', verbose_name=u'Привязка к галерее', default=None)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'Время создания')
    last_changes = models.DateTimeField(auto_now=True, verbose_name=u'Время последнего редактирования')

    class Meta:
        verbose_name = u'Творение'
        verbose_name_plural = u'Творения'
        ordering = ('-created_at',)
