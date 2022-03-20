# 会员移动端路由文件配置
from django.urls import path
from mobile.views import index

urlpatterns = [
    path('', index.index, name='mobile_index'),
]
