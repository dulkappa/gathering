# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic.list import ListView
from cms.forms import CollectionForm, ItemForm
from cms.models import Collection, Item

def collection_list(request):
    '''コレクションの一覧'''
    collections = Collection.objects.all().order_by('id')
    return render_to_response('cms/collection_list.html', {'collections': collections}, context_instance=RequestContext(request))

def collection_edit(request, collection_id=None):
    '''コレクションの編集'''
    if collection_id:
      collection = get_object_or_404(Collection, pk=collection_id)
    else:
      collection = Collection()

    if request.method == 'POST':
      form = CollectionForm(request.POST, instance=collection)

      if form.is_valid():
        collection = form.save(commit=False)
        collection.save()
        return redirect('cms:collection_list')
    else:
      form = CollectionForm(instance=collection)

    return render_to_response('cms/collection_edit.html', dict(form=form, collection_id=collection_id), context_instance=RequestContext(request))

def collection_del(request, collection_id):
    '''コレクションの削除'''
    collection = get_object_or_404(Collection, pk=collection_id)
    collection.delete()
    return redirect('cms:collection_list')

class ItemList(ListView):
  '''アイテムの一覧'''
  context_object_name = 'items'
  template_name = 'cms/item_list.html'
  paginate_by = 5

  def get(self, request, *args, **kwargs):
    collection = get_object_or_404(Collection, pk=kwargs['collection_id'])
    items = collection.items.all().order_by('id')
    self.object_list = items

    context = self.get_context_data(object_list=self.object_list, collection=collection)
    return self.render_to_response(context)

def item_edit(request, collection_id, item_id=None):
  '''アイテムの編集'''
  collection = get_object_or_404(Collection, pk=collection_id)
  if item_id:
    item = get_object_or_404(Item, pk=item_id)
  else:
    item = Item()

  if request.method == 'POST':
    form = ItemForm(request.POST, instance=item)
    if form.is_valid():
      item = form.save(commit=False)
      item.collection = collection
      item.save()
      return redirect('cms:item_list', collection_id=collection_id)
  else:
    form = ItemForm(instance=item)

  return render_to_response('cms/item_edit.html', dict(form=form, collection_id=collection_id, item_id=item_id), context_instance=RequestContext(request))

def item_del(request, collection_id, item_id):
    '''アイテムの削除'''
    item = get_object_or_404(item, pk=item_id)
    item.delete()
    return redirect('cms:item_list', collection_id=collection_id)
