def sidebar_permissions(request):
    user = request.user
    if not user.is_authenticated:
        return {}

    is_super = user.is_superuser

    sidebar_perms = {
        "dashboard": is_super or user.has_perm("accounts.view_dashboard"),
        "hub": is_super or user.has_perm("hub.view_hub"),
        "demo": is_super or user.has_perm("demo.view_demo"),
        "setup": is_super or user.has_perm("setup.view_setup"),
    }

    current_app = getattr(request.resolver_match, "app_name", "")

    active_parent = {
        "dashboard": current_app == "accounts",
        "hub": current_app == "demo",
        "demo": current_app == "demo",
        "setup": current_app == "setup",
    }

    return {
        "sidebar_perms": sidebar_perms,
        "active_parent": active_parent,
    }
