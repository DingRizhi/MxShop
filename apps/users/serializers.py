# _*_ coding:utf-8 _*_
__author__ = 'imbaqian'
__date__ = '2018/7/20 16:30'

from datetime import datetime
from  datetime import timedelta
from .models import VerifyCode
import re
from MxShop.settings import REGEX_MOBILE

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
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


class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(label="验证码", required=True, write_only=True, max_length=4, min_length=4,
                                 error_messages={
                                     "blank":"请输入验证码",
                                     "required":"请输入验证码",
                                     "max_length":"验证码格式错误",
                                     "min_length":"验证码格式错误",
                                 },
                                 help_text='验证码')
    username = serializers.CharField(label="用户名",required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(),message="用户已存在",)])
    password = serializers.CharField(label="密码", style={'input_type': 'password'}, write_only=True)
    def validate_code(self, code):
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data['username']).order_by('-add_time')
        if verify_records:
            last_record = verify_records[0]
            five_min_age = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_min_age > last_record.add_time:
                raise serializers.ValidationError('验证码过期')
            if last_record.code !=  code:
                raise  serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        attrs['mobile'] = attrs['username']
        del attrs['code']
        return attrs

    def create(self, validated_data):
        """
        原来的create没有将密码加密,在这里重载create 将密码加密
        只在post的时候生效
        """
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'code', 'mobile', 'password')