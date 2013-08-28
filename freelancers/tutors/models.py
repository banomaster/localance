from django.core.urlresolvers import reverse
from django.db import models
from freelancers.models import Freelancer


class ListTutorSkills(models.Model):
	skill = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.skill

class ListTutorClients(models.Model):
	client = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.client
		
class Tutor(Freelancer):
	clients = models.ManyToManyField(ListTutorClients)
	skills = models.ManyToManyField(ListTutorSkills)

	def get_absolute_url(self):
		return reverse("detail_tutor", kwargs={"slug":self.slug})