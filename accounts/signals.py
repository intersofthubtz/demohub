from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission, User

@receiver(post_migrate)
def create_or_update_groups(sender, **kwargs):
    """
    Create/update roles and assign permissions automatically.
    """
    # Define permissions per role
    role_permissions = {
        "Administrator": "__all__",
        'DemoUser': ['view_demo'],
        'HubUser': ['view_hub'],
        'SetupUser': ['view_setup'],
    }

    all_permissions = Permission.objects.all()

    for group_name, perm_codenames in role_permissions.items():
        group, _ = Group.objects.get_or_create(name=group_name)

        if perm_codenames == "__all__":
            group.permissions.set(all_permissions)
        else:
            valid_permissions = Permission.objects.filter(codename__in=perm_codenames)
            group.permissions.set(valid_permissions)

        group.save()

        # Optional: auto-assign superuser for Administrator
        if group_name == "Administrator":
            for user in User.objects.filter(groups__name="Administrator"):
                user.is_superuser = True
                user.is_staff = True
                user.user_permissions.set(all_permissions)
                user.save()
