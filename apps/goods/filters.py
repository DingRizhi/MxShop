# _*_ coding:utf-8 _*_
__author__ = 'imbaqian'
__date__ = '2018/7/12 22:58'

from django_filters import rest_framework as filter
from .models import Goods


class GoodsFilter(filter.FilterSet):
    """
    商品的过滤类
    """
    price_min = filter.NumberFilter(name="shop_price", lookup_expr="gte")
    price_max = filter.NumberFilter(name="shop_price", lookup_expr="lte")
    name = filter.CharFilter(name="name", lookup_expr="icontains")

    class  Meta:
        model = Goods
        fields = [ 'name']