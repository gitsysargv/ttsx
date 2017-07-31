from django.shortcuts import render


def login(request):
    return render(request, 'tt_user/login.html')


def register(request):
    return render(request, 'tt_user/register.html')
