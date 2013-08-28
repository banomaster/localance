from django.core.urlresolvers import reverse
from django.db import models
from freelancers.models import Freelancer


class ListPhotographerSkills(models.Model):
	skill = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.skill

class ListPhotographerClients(models.Model):
	client = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.client

class Photographer(Freelancer):
	clients = models.ManyToManyField(ListPhotographerClients)
	picture_portfolio = models.ImageField(upload_to='uploads/portfolio/photographers', max_length=100)
	skills = models.ManyToManyField(ListPhotographerSkills)

	def get_absolute_url(self):
		return reverse("detail_photographer", kwargs={"slug":self.slug})