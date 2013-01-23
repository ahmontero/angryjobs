# -*- encoding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _

from web.models import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(label=_("Comment"),
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 5,
            'class': 'span11', 'placeholder': 'Comentario'}))

    class Meta:
        model = Comment
