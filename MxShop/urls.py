"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# coding:utf-8
from django.urls import path,re_path
import  xadmin
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
from django.urls import include
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from goods.views import GoodsListViewSet, GoodsCategoryViewSet
from users.views import SmsCodeViewSet, UserViewSet
from user_operation.views import UserFavViewSet
from rest_framework_jwt.views import obtain_jwt_token

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

# 配置goods的url
router.register('goods', GoodsListViewSet, base_name="goods")

# 配置category的url
router.register('categorys', GoodsCategoryViewSet, base_name="categorys")

# 配置verify code的url
router.register('code', SmsCodeViewSet, base_name="code")

# 配置注册users 的url
router.register('users', UserViewSet, base_name="users")

# 配置注册user fav 的url
router.register('userfavs', UserFavViewSet, base_name="userfavs")


urlpatterns = [
    path('', include(router.urls)),
    path('xadmin/', xadmin.site.urls),
    # media文件处理
    re_path('media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # 富文本相关url
    path('ueditor/', include('DjangoUeditor.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title="慕雪生鲜")),
    # rest 自带token
    path('api-token-auth/', views.obtain_auth_token),
    # jwt token验证
    path('login/', obtain_jwt_token),
]
