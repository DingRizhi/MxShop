from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import VerifyCode
from .serializers import SmsSerializer
from MxShop.settings import APIKEY
from utils.yunpian import YunPian
# Create your views here.

User = get_user_model()


class CumstomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位随机验证码
        """
        from random import choice
        seeds = '0123456789'
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data['mobile']
        yun_pian = YunPian(APIKEY)
        code = self.generate_code()
        sms_status = yun_pian.send(code=code, mobile=mobile)
        if sms_status["code"] == 0:
            # 验证码发送成功
            VerifyCode(code=code, mobile=mobile).save()
            return Response(
                data={
                    "mobile":mobile,
                },
                status = status.HTTP_201_CREATED
            )
        else:
            # 验证码发送失败
            return Response(
                data={
                    "mobile":sms_status["msg"]
                },
                status = status.HTTP_400_BAD_REQUEST
            )