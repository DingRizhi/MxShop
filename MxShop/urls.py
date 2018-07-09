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
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # media文件处理
    re_path('media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # 富文本相关url
    path('ueditor/', include('DjangoUeditor.urls')),
]
