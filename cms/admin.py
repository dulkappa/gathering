# -*- coding: utf-8 -*-
from django.contrib import admin
from cms.models import Collection, Item

# admin.site.register(Collection)
# admin.site.register(Item)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'saummary',)  # 一覧に出したい項目
    list_display_links = ('id', 'name',)  # 修正リンクでクリックできる項目
admin.site.register(Collection, CollectionAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
admin.site.register(Item, ItemAdmin)
