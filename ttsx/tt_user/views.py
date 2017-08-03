from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1
from django.http import JsonResponse
from .decorator import logined
u = UserInfo()
u.save()

'''
    header_top为模板顶部显示用户信息， 登录 和注册不用显示
'''


def login(request):
    # print(request.COOKIES)
    uname = request.COOKIES.get('remember', '')  # 这里取一下浏览器保存德cookie
    return render(request, 'tt_user/login.html', {'header_top': '0', 'username': uname})


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


@logined
def user_center_info(request):
    uid = request.session.get('uid')
    uname = request.session.get('uname')
    info = UserInfo.objects.filter(id=uid)

    d = {'uname': uname, 'info': info}
    return render(request, 'tt_user/user_center_info.html', d)


@logined
def user_center_order(request):
    uname = request.session.get('uname')

    d = {'uname': uname}
    return render(request, 'tt_user/user_center_order.html', d)


@logined
def site(request):
    uid = request.session.get('uid')
    uname = request.session.get('uname')
    # info = UserInfo.objects.filter(id=uid)
    '''这里save不成功 , 得用上filter'''
    info = UserInfo.objects.get(id=uid)


    '''当有POST请求时进行用户数据的保存'''
    if request.method == 'POST':
        info.name = request.POST.get('name')
        info.addr = request.POST.get('addr')
        info.phone = request.POST.get('phone')
        info.save()  # 记住要保存，用save()


    d = {'uname': uname, 'info': info}
    return render(request, 'tt_user/user_center_site.html', d)


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

    '''登录成功后保存一下用户信息--> id ,用户名。  而如果用户勾选记住用户名，则存一下COOKIES，'''
    request.session['uid'] = info[0].id
    request.session['uname'] = info[0].uname
    remember = request.POST.get('remember', '0')
    response = redirect(user_path)  # 用重定向也能返回response，记住响应对象，从哪里来的哪里去
    if remember == '1':
        response.set_cookie('remember', uname, max_age=60*60*24*3)
    else:
        response.set_cookie('remember', '', max_age=-1)
    return response


def user_center_order(request):
    pass


def user_center_site(request):
    pass
