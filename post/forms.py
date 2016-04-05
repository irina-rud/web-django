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

class PostSearchSortForm(forms.Form):
    search = forms.CharField(label=u'Поиск ', max_length=255)
    sort_field = forms.ChoiceField(choices=(("id", "ID"), ("created_at", u'Дата создания'), ('last_changes', u'Дата последнего изменения')))
    def clean(self):
        raise forms.ValidationError(u'уходи. Мне надоело искать по несуществующим полям.')