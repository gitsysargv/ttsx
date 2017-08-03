from django.shortcuts import redirect


# 判断是否登录的装饰器
def logined(func):
    def fn_inline(request, *args, **kwargs):
        if 'uid' in request.session:

            return func(request, *args, **kwargs)

        else:

            return redirect('/tt_user/login/')
    return fn_inline