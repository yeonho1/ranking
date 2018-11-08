#-*coding:utf-8-*
from __future__ import unicode_literals
from django import forms
from .models import Ranker


class RankerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RankerForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(label=u'이름')
        self.fields['rank'] = forms.IntegerField(label=u'순위')
        self.fields['additions'] = forms.CharField(label=u'비고')
    
    class Meta:
        fields = ['name', 'rank', 'additions']
