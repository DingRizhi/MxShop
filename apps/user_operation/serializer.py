# _*_ coding:utf-8 _*_
__author__ = 'imbaqian'
__date__ = '2018/7/23 15:44'

from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers
from .models import UserFav


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已收藏"
            )
        ]
        fields = ('user', 'goods', 'id')
