from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_user_groups(allowed_groups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.groups.exists():
                for group in request.user.groups.all():
                    if group.name in allowed_groups:
                        return view_func(request, *args, **kwargs)
                return redirect('main:home')
            else:
                return redirect('users:login')
        return wrapper_func
    return decorator