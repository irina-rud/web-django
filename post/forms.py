# coding: utf-8
from django import forms

from post.models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import FormActions

class PostForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Отправить'))
    class Meta:
        model = Post
        fields = ('title', 'sign', 'picture', 'is_published', 'gallery')

class SearchForm(forms.Form):
    query = forms.CharField(label=u'Поиск: ', max_length=100)