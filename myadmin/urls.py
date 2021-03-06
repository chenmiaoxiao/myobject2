# 后台路由文件配置
from django.urls import path
from myadmin.views import index
from myadmin.views import user
from myadmin.views import shop

urlpatterns = [
    path('', index.index, name='myadmin_index'),  # 后台首页

    # 后台管理员登录、退出路由配置
    path('login', index.login, name='myadmin_login'),  # 加载登录表单
    path('dologin', index.dologin, name='myadmin_dologin'),  # 执行登录
    path('logout', index.logout, name='myadmin_logout'),  # 退出
    path('verify', index.verify, name='myadmin_verify'),  # 输出验证码

    # 员工信息管理路由
    path('user/<int:pIndex>', user.index, name='myadmin_user_index'),  # 浏览
    path('user/add', user.add, name='myadmin_user_add'),  # 加载添加表单
    path('user/insert', user.insert, name='myadmin_user_insert'),  # 执行添加
    path('user/del/<int:uid>', user.delete, name='myadmin_user_delete'),  # 执行删除
    path('user/edit/<int:uid>', user.edit, name='myadmin_user_edit'),  # 加载编辑表单
    path('user/update/<int:uid>', user.update, name='myadmin_user_update'),  # 执行编辑

    # 店铺路由
    path('shop/<int:pIndex>', shop.index, name="myadmin_shop_index"),
    path('shop/add', shop.add, name="myadmin_shop_add"),
    path('shop/insert', shop.insert, name="myadmin_shop_insert"),
    path('shop/del/<int:sid>', shop.delete, name="myadmin_shop_del"),
    path('shop/edit/<int:sid>', shop.edit, name="myadmin_shop_edit"),
    path('shop/update/<int:sid>', shop.update, name="myadmin_shop_update"),

]
# from django_redis import get_redis_connection