from django.contrib.auth.decorators import login_required
from common.decorators import permission_required_redirect
from django.shortcuts import render

@login_required
@permission_required_redirect("setup.view_setup")
def setup(request):
    message = "Welcome to Setup section!"
    return render(request, "setup/setup.html", {"message": message})
