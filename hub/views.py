from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from common.decorators import permission_required_redirect

@login_required
@permission_required_redirect("hub.view_hub")
def hub_list(request):
    message = "Welcome to Hub section!"
    return render(request, "hub/hub_list.html", {"message": message})
