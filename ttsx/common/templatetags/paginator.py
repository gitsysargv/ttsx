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
from django.template import Library

register = Library()  # 从Library类中创建了一个注册对象


@register.filter
def page_list(page):
    print('-----------------------')
    d = {}
    page_bottom = page.paginator.num_pages
    index = page.number
    if page_bottom > 5:
        if index >= 3 and index <= page_bottom - 2:
            d['range'] = [index - 2, index - 1, index, index + 1, index + 2]
        elif index < 3:
            d['range'] = [1, 2, 3, 4, 5]
        else:
            d['range'] = [page_bottom - 4, page_bottom - 3, page_bottom - 2, page_bottom - 1, page_bottom]
    else:
        d['range'] = page.paginator.page_range
    print(d['range'])
    return d['range']
