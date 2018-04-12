# coding=utf-8
from haystack import indexes
from .models import Test


class TestIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Test

    def index_queryset(self, using=None):
        return self.get_model().objects.all()