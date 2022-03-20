# 员工信息管理视图文件
import time

from django.shortcuts import render  # 渲染模块
from django.http import HttpResponse
from myadmin.models import Shop
from django.core.paginator import Paginator  # 分页模块
from datetime import datetime


# Create your views here.

def index(request,pIndex=1):
    # 浏览信息
    smod = Shop.objects
    li = smod.filter(status__lt=9)  # status<9，过滤status=9的数据 即对数据库中的数据进行状态性的删除，实际数据还存在

    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(li, 5)  # 每页5条数据
    maxpages = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 获取当前页数据
    plist = page.page_range  # 获取页码列表信息
    context = {'shop_list':list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages}
    return render(request,'myadmin/shop/index.html',context)

def add(request):
    # 加载信息添加表单
    return render(request, 'myadmin/shop/add.html')

def insert(request):
    # 执行信息添加
    try:
        # 店铺封面图片的上传处理
        myfile = request.FILES.get("cover_pic", None)
        if not myfile:
            return HttpResponse("没有店铺封面上传文件信息")
        cover_pic = str(time.time()) + "." + myfile.name.split('.').pop()
        destination = open("./static/uploads/shop/" + cover_pic, "wb+")
        for chunk in myfile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        # 店铺logo图片的上传处理
        myfile = request.FILES.get("banner_pic", None)
        if not myfile:
            return HttpResponse("没有店铺logo上传文件信息")
        banner_pic = str(time.time()) + "." + myfile.name.split('.').pop()
        destination = open("./static/uploads/shop/" + banner_pic, "wb+")
        for chunk in myfile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        # 实例化model,封装信息，并执行添加操作
        ob = Shop()
        ob.name = request.POST['name']
        ob.address = request.POST['address']
        ob.phone = request.POST['phone']
        ob.cover_pic = cover_pic
        ob.banner_pic = banner_pic
        ob.status = 1
        ob.create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info':'添加成功！'}
    except Exception as err:
        print(err)
        context = {'info': '添加失败！'}
    return render(request, 'myadmin/info.html', context)

def delete(request,sid=0):
    # 执行信息删除
    try:
        ob = Shop.objects.get(id=sid)
        ob.status = 9
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info': '删除成功！'}
    except Exception as err:
        print(err)
        context = {'info': '删除失败！'}
    return render(request, 'myadmin/info.html', context)

def edit(request, sid=0):
    # 加载信息编辑表单
    try:
        ob = Shop.objects.get(id=sid)
        context = {'shop': ob}
        return render(request, 'myadmin/shop/edit.html', context)
    except Exception as err:
        print(err)
        context = {'info': '未找到要修改的信息！'}
        return render(request, 'myadmin/info.html', context)

def update(request, sid=0):
    # 执行信息编辑
    try:
        ob = Shop.objects.get(id=sid)
        ob.name = request.POST['name']
        ob.address = request.POST['address']
        ob.phone = request.POST['phone']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info': '修改成功！'}
    except Exception as err:
        print(err)
        context = {'info': '修改失败！'}
    return render(request, 'myadmin/info.html', context)
