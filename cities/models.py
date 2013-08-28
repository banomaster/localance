from core.models import TimeStampedModel
from django.db import models
from django.template.defaultfilters import slugify

class City(TimeStampedModel):
	name = models.CharField (max_length = 50)
	slug = models.SlugField(max_length=255,blank=True,default='')
	description = models.TextField()

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(City,self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("city", kwargs={"slug_city":self.slug})