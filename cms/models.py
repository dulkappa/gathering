# -*- coding:utf-8 -*-
from django.db import models

class Collection(models.Model):
  '''コレクション'''
  name = models.CharField(u'コレクション名', max_length=255)
  saummary = models.TextField(u'概要', blank=True)

  def __unicode__(self):
    return self.name

class Item(models.Model):
  '''項目'''
  collection = models.ForeignKey(Collection, verbose_name=u'コレクション', related_name='items')
  name = models.CharField(u'項目名', max_length=255)

  def __unicode__(self):
    return self.name
