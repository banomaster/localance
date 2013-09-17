from accounts.models import UserAccount
from oauth2 import Token
 
from social_auth.backends.utils import build_consumer_oauth_request
from social_auth.backends.facebook import FacebookAuth

from urlparse import urlparse 
import urllib2 
from django.core.files import File
  #add imprt of content file wrapper
from django.core.files.base import ContentFile

def load_avatar(backend, response, user, profile=None, *args, **kwargs):
    if profile:
        if backend.name == "facebook":
            url = "http://graph.facebook.com/%s/picture?width=200&height=200" % response['id']
          
            name = urlparse(url).path.split('/')[-2] + ".jpg"
            #wrap your file content
            content = ContentFile(urllib2.urlopen(url).read())
            profile.avatar.save(name, content, save=True)
        else:
            raise ValueError()

def testing(user, details, *args, **kwargs):
    print details['username']

    return


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
