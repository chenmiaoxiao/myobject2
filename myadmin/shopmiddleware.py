# 中间件的编写，从django官网复制模板加以改写需求
from django.shortcuts import redirect
from django.urls import reverse

import re
class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        path = request.path
        # print('url:', path)

        # 判断管理后台是否登录
        # 定义后台不登录也可直接访问的url列表
        urllist = ['/myadmin/login', '/myadmin/dologin', '/myadmin/logout', '/myadmin/verify']
        # 判断当前请求url地址是否以/myadmin开头，并且不在urllist中，才做是否转登录操作
        if re.match(r'^/myadmin', path) and (path not in urllist):
            # 判断用户是否登录(在session中是否有'adminuser')
            if 'adminuser' not in request.session:
                # 重定向到登录页
                return redirect(reverse('myadmin_login'))

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
