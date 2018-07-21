from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = "用户管理" # 控制xadmin 左侧菜单栏名称显示

    # 通过信号量修改,会有bug,在xamin里添加用户时候会把密码加密两次
    # def ready(self):
    #     import users.signals