from accounts.models import UserAccount
from core.models import TimeStampedModel
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from freelancers.models import Freelancer

class Inquiry(TimeStampedModel):
	user = models.ForeignKey(UserAccount)
	freelancer = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey('freelancer', 'object_id')
	description = models.TextField()

	class Meta:
		abstract = True