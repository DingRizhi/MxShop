# _*_ coding:utf-8 _*_
__author__ = 'imbaqian'
__date__ = '2018/7/12 15:18'

from rest_framework import serializers
from .models import Goods, GoodsCategory


class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ("name",)


class GoodsSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()
    class Meta:
        model = Goods
        #fields = ('category', 'goods_sn', 'name', 'click_num', 'goods_front_image', 'add_time')
        fields = "__all__"