from django.shortcuts import render, redirect
from .models import GoodsInfo, TypeInfo
from django.core.paginator import Paginator


def index(request):
    type_list = TypeInfo.objects.all()
    list = []
    for type in type_list:
        list.append({'type_list': type,
                     'click_list': type.goodsinfo_set.order_by('-gclick')[0:3],
                     'new_list': type.goodsinfo_set.order_by('-id')[0:4],
                     })
    d = {}
    d['car'] = '1'
    d['list'] = list
    return render(request, 'tt_goods/index.html', d)


def list(request, type_id, index, order_by):
    '''
    列表页以传递来的参数进行排列， list/1_1_1  ，
    分别表示：类型， 页面下标，排列方式
    '''
    d = {}
    index = int(index)
    type_info = TypeInfo.objects.get(pk=type_id)
    '''加上一个排序类型判断，定义一个排序类型字符串，1：id， 2：价格，3：点击量'''
    order_bystr = '-id'
    if order_by == '2':
        order_bystr = 'gprice'
    elif order_by == '3':
        order_bystr = '-gclick'
    d['order_by'] = order_by

    goods_list = type_info.goodsinfo_set.order_by(order_bystr)
    page_container = Paginator(goods_list, 10)
    page_bottom = page_container.num_pages
    d['page_bottom'] = page_bottom
    if index > page_bottom:
        return render(request, '404.html')

    new_list = type_info.goodsinfo_set.order_by('-id')[0:2]
    d['type'] = type_info
    d['new_list'] = new_list
    page_list = page_container.page(index)
    d['page_list'] = page_list
    # 当页数大于5的时候进行分页，只传递5页；
    if page_bottom > 5:
        if index >= 3 and index <= page_bottom - 2:
            d['range'] = [index - 2, index - 1, index, index + 1, index + 2]
        elif index < 3:
            d['range'] = [1, 2, 3, 4, 5]
        else:
            d['range'] = [page_bottom - 4, page_bottom - 3, page_bottom - 2, page_bottom - 1, page_bottom]
    else:
        d['range'] = page_container.page_range
    d['car'] = '1'
    d['index'] = index
    return render(request, 'tt_goods/list.html', d)


def detail(request, gid):
    d = {}
    try:
        goods = GoodsInfo.objects.get(pk=gid)
        new_list = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
        d['goods'] = goods
        d['new_list'] = new_list
        return render(request, 'tt_goods/detail.html', d)
    except Exception as e:
        print(e)
        return render(request, '404.html')


def demo(request):
    return render(request, 'demo.html')


from haystack.generic_views import SearchView


class MySearchView(SearchView):
    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        context['car'] = '1'
        # context['isleft'] = '0'
        return context
