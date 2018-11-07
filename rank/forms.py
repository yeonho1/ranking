#-*coding:utf-8-*
from __future__ import unicode_literals
from django import forms
from .models import Ranker


class RankerForm(forms.Form):
    def validate(value):
        if str(value).rstrip().lstrip() == '':
            raise forms.ValidationError(u'필수사항입니다.')
    def __init__(self, *args, **kwargs):
        super(RankerForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(label=u'이름', validators=[self.validate])
        self.fields['rank'] = forms.IntegerField(label=u'순위', validators=[self.validate])
        self.fields['additions'] = forms.CharField(label=u'비고', validators=[self.validate])
    
    class Meta:
        fields = ['name', 'rank', 'additions']