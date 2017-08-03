from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1
from django.http import JsonResponse


def login(request):
    return render(request, 'tt_user/login.html', {'header_top': '0'})


def handle(request):
    d = request.POST
    uname = d.get('user_name')
    upwd = d.get('pwd')
    ucpwd = d.get('cpwd')
    email = d.get('email')

    if upwd != ucpwd:
        return redirect('tt_user/register.html', {'header_top': '0'})

    s1 = sha1()
    s1.update(upwd.encode())
    pwd_hash = s1.hexdigest()

    info = UserInfo()
    info.uname = uname
    info.upwd = pwd_hash
    info.email = email
    info.save()
    return render(request, 'tt_user/login.html', {'header_top': '0'})


def register(request):
    return render(request, 'tt_user/register.html', {'header_top': '0'})


def reuse(request):
    get_name = request.GET.get('uname')
    print(get_name)
    info = UserInfo.objects.filter(uname=get_name)
    if info:
        # 当数据库中有重名的用户名时返回一个错误
        return JsonResponse({'reuse': 1})
    else:
        return JsonResponse({'reuse': 0})


def user_center_info(request):

    return render(request, 'tt_user/user_center_info.html')


def login_handle(request):
    user_path = request.session.get('user-path', '/')  # 取出session里边存储的前一次路径
    uname = request.POST.get('username')
    upwd = request.POST.get('pwd')

    info = UserInfo.objects.filter(uname=uname)
    if len(info) == 0:
        # 当有错误的时候传递数据给模板，传之前错误的名字
        return render(request, 'tt_user/login.html', {'user_error': 1, 'username': uname, 'header_top': '0'})
    else:
        s1 = sha1()
        s1.update(upwd.encode())
        upwd_sha1 = s1.hexdigest()
        if info[0].upwd != upwd_sha1:
            return render(request, 'tt_user/login.html', {'pwd_error': 1, 'upwd': upwd, 'header_top': '0'})
    return redirect(user_path)


def user_center_order(request):
    pass


def user_center_site(request):
    pass
