from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from common.decorators import permission_required_redirect

@login_required
@permission_required_redirect("accounts.view_demo")
def demo_list(request):
    message = "Here are all demo items."
    return render(request, "demo/demo_list.html", {"message": message})
