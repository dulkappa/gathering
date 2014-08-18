# -*- coding:utf-8 -*-
from django.test import TestCase

from cms.models import Collection

class CollectionTests(TestCase):

  def test_is_collection_added(self):
    collection = Collection(name='test', summary='a sample collection for test.')
    self.assertEqual(len(collection.name), 4)
