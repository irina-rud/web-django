# coding: utf-8
from __future__ import unicode_literals

from django.db import models


class Comment(models.Model):
	text = models.TextField(verbose_name=u'Текст комменария')
	post = models.ForeignKey('post.Post')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания')


	class Meta:
		verbose_name = u'Комментарий'
		verbose_name_plural = u'Комментарии'
		ordering = ('-created_at',)