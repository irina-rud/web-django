# coding: utf-8
from django import forms

from gallery.models import Gallery


class GalleryForm(forms.Form):
    class Meta:
        model = Gallery
        fields = ('title')


class SearchForm(forms.Form):
    query = forms.CharField(label=u'Поиск: ', max_length=100)


class PostSearchSortForm(forms.Form):
    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(
        choices=(("id", "ID"), ("created_at", u'Дата создания'), ('last_changes', u'Дата последнего изменения')))

    def clean(self):
        raise forms.ValidationError(u'уходи. Мне надоело искать по несуществующим полям.')
