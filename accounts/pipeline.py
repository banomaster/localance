from accounts.models import UserAccount

def create_profile(user=None, profile=None, *args, **kwargs):
    """
    Create user profile if necessary
    """

    if profile:
        return { 'profile': profile}
    if not user:
        return
    return { 'profile': UserAccount.objects.get_or_create(user=user)[0] }

def set_guardian_permissions(user=None, profile=None, *args, **kwargs):
    """
    Give the user permission to modify themselves
    """
    if not user or not user.is_authenticated():
        return
    if profile:
        # Give permissions to view and change profile
        for perm in ASSIGNED_PERMISSIONS['profile']:
            assign(perm[0], user, profile)

    # Give permissions to view and change itself
    for perm in ASSIGNED_PERMISSIONS['user']:
        assign(perm[0], user, user)
