from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1
from django.http import JsonResponse


def login(request):
    return render(request, 'tt_user/login.html')


def handle(request):
    d = request.POST
    uname = d.get('user_name')
    upwd = d.get('pwd')
    ucpwd = d.get('cpwd')
    email = d.get('email')

    if upwd != ucpwd:
        return redirect('tt_user/register.html')

    s1 = sha1()
    s1.update(upwd.encode())
    pwd_hash = s1.hexdigest()

    info = UserInfo()
    info.uname = uname
    info.upwd = pwd_hash
    info.email = email
    info.save()
    return render(request, 'tt_user/login.html')


def register(request):
    return render(request, 'tt_user/register.html')


def reuse(request):
    get_name = request.GET.get('uname')
    print(get_name)
    info = UserInfo.objects.filter(uname=get_name)
    if info:
        return JsonResponse({'reuse': 1})
    else:
        return JsonResponse({'reuse': 0})
