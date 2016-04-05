# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Владелец')

    class Meta:
        verbose_name = u'Галерея'
        verbose_name_plural = u'Галереи'

    def __unicode__(self):
        return self.title
