class MidWare:
    def process_view(self, request, view_func, view_args, view_kwargs):

        request.session['user-path'] = request.path
