# 前台大堂路由文件配置
from django.urls import path
from web.views import index

urlpatterns = [
    path('', index.index, name='web_index'),
]
