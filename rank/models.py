# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Ranker(models.Model):
    name = models.CharField(max_length=30, verbose_name="성명")
    rank = models.IntegerField(verbose_name="순위")
    additions = models.CharField(max_length=255, verbose_name="비고", default=u'없음')

    def __str__(self):
        return self.__unicode__()
    
    def __unicode__(self):
        return u'%s (%d위)' % (self.name, self.rank)
    
    class Meta:
        verbose_name = 'Ranker'
        verbose_name_plural = 'Rankers'