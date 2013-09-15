from accounts.models import UserAccount
from oauth2 import Token
 
from social_auth.backends.utils import build_consumer_oauth_request
from social_auth.backends.facebook import FacebookAuth

def load_data_new_user(backend, response, user, *args, **kwargs):
    if user is None:
        if backend.name == "facebook":
            try:
                url = "http://graph.facebook.com/%s/picture?width=200&height=200&redirect=false" % response['id']
                data = json.loads(urllib2.urlopen(url).read())['data']
                return {'avatar': data}
            except StandardError:
                return {'avatar': None}
        else:
            raise ValueError()


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
