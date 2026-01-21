from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout
from .forms import LoginForm
from common.decorators import permission_required_redirect

def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:dashboard")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("accounts:dashboard")
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("accounts:login")


@login_required
@permission_required_redirect("accounts.view_dashboard")
def dashboard(request):
    message = "Welcome to your Dashboard!"
    return render(request, "accounts/dashboard.html", {"message": message})


@login_required
def unauthorized(request):
    """Plain page with no sidebar, redirects to login/logout."""
    return render(request, "accounts/unauthorized.html")
