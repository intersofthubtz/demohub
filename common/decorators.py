from functools import wraps
from django.shortcuts import redirect
from django.conf import settings

def permission_required_redirect(perm):
    """
    Decorator to check:
      1. Authenticated user – if not, redirect to logout page (clears session).
      2. Permission check – if user lacks permission, redirect to unauthorized page.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Redirect unauthenticated users to logout (session cleared)
            if not request.user.is_authenticated:
                logout_url = settings.LOGOUT_REDIRECT_URL or '/accounts/logout/'
                return redirect(logout_url)

            # Redirect users without permission to unauthorized page
            if not request.user.has_perm(perm):
                return redirect('accounts:unauthorized')

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
