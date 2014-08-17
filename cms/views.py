# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from cms.forms import CollectionForm
from cms.models import Collection

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
