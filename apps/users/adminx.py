# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/2/14 0014 01:17'


import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    """
    全局设置
    """
    site_title = "生鲜超市后台管理系统"
    site_footer = "CreateBy imbaqian"
    # menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)