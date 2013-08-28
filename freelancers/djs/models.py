from django.core.urlresolvers import reverse
from django.db import models
from freelancers.models import Freelancer


class ListDJGenres(models.Model):
	genre = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.genre

class ListDJOccasions(models.Model):
	occasion = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.occasion
		
class DJ(Freelancer):
	occasions = models.ManyToManyField(ListDJOccasions)
	genres = models.ManyToManyField(ListDJGenres)
	soundcloud_profile = models.URLField(max_length = 50)
	picture_portfolio = models.ImageField(upload_to='upload/portfolio/DJ',max_length=100)

	def get_absolute_url(self):
		return reverse("detail_dj", kwargs={"slug":self.slug})