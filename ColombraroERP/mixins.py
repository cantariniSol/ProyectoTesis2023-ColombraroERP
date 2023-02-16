from django.shortcuts import redirect

class IsSuperUserMixins(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('erp:dashboard')
