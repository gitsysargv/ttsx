#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "chaiming"
__mtime__ = "2017/8/5"
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓ ┏┓
┏┛┻━━━┛┻┓
┃ ☃ ┃
┃ ┳┛ ┗┳ ┃
┃ ┻ ┃
┗━┓ ┏━┛
┃ ┗━━━┓
┃ 神兽保佑 ┣┓
┃　永无BUG！ ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫ ┃┫┫
┗┻┛ ┗┻┛
"""
from haystack import indexes
from .models import GoodsInfo


# 指定对于某个类的某些数据建立索引
class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return GoodsInfo

    # 索引的过滤
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
