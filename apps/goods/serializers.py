# _*_ coding:utf-8 _*_
__author__ = 'imbaqian'
__date__ = '2018/7/12 15:18'

from rest_framework import serializers
from .models import Goods, GoodsCategory


class GoodsCategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsCategorySerializer2(serializers.ModelSerializer):
    sub_cat = GoodsCategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsCategorySerializer(serializers.ModelSerializer):
    sub_cat = GoodsCategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()
    class Meta:
        model = Goods
        #fields = ('category', 'goods_sn', 'name', 'click_num', 'goods_front_image', 'add_time')
        fields = "__all__"
