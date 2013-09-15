from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
    user = models.OneToOneField(User,
                                unique=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

    avatar = models.ImageField(
    					blank = True,
    					null = True,
    					upload_to='uploads',
    					)

    def __unicode__(self):
    	return self.user.username
    
