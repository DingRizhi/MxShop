# _*_ coding:utf-8 _*_
__author__ = 'imbaqian'
__date__ = '2018/7/20 16:30'

from datetime import datetime
from  datetime import timedelta
from .models import VerifyCode
import re
from MxShop.settings import REGEX_MOBILE

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        """
        # 验证是否注册过
        if User.objects.filter(mobile=mobile).count():
            raise  serializers.ValidationError("用户已经存在")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        # 验证发送频率
        one_min_age = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_min_age, mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60秒")

        return mobile