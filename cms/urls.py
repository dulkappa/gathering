# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from cms import views

urlpatterns = patterns('',
    # コレクション
    url(r'^collection/$', views.collection_list, name='collection_list'),   # 一覧
    url(r'^collection/add/$', views.collection_edit, name='collection_add'),  # 登録
    url(r'^collection/mod/(?P<collection_id>\d+)/$', views.collection_edit, name='collection_mod'),  # 修正
    url(r'^collection/del/(?P<collection_id>\d+)/$', views.collection_del, name='collection_del'),   # 削除

    # アイテム
    url(r'^item/(?P<collection_id>\d+)/$', views.ItemList.as_view(), name='item_list'),  # 一覧
    url(r'^item/add/(?P<collection_id>\d+)/$', views.item_edit, name='item_add'),        # 登録
    url(r'^item/mod/(?P<collection_id>\d+)/(?P<item_id>\d+)/$', views.item_edit, name='item_mod'),  # 修正
    url(r'^item/del/(?P<collection_id>\d+)/(?P<item_id>\d+)/$', views.item_del, name='item_del'),   # 削除
)
