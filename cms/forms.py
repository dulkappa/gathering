# -*- coding: utf-8 -*-
from django.forms import ModelForm
from cms.models import Collection, Item

class CollectionForm(ModelForm):
    '''コレクションのフォーム'''
    class Meta:
        model = Collection
        fields = ('name', 'summary', )

class ItemForm(ModelForm):
    '''アイテムのフォーム'''
    class Meta:
        model = Item
        fields = ('name', )
