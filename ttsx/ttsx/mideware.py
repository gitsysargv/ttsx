class MidWare:
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path not in [
            '/tt_user/login/',
            '/tt_user/register/',
            '/tt_user/handle/',
            '/tt_user/login_handle/',
            '/tt_user/logout/',
        ]:
            request.session['user-path'] = request.get_full_path()
        # print('-'*20)
        # print(request.session['user-path'])
        # print('='*20)
