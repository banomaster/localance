from cities.models import City
from core.models import TimeStampedModel
from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

class Category(TimeStampedModel):
	name = models.CharField (max_length = 30)
	description = models.TextField()
	cover_picture = models.ImageField(upload_to='content/categories/normal',max_length=100)
	slug = models.SlugField(max_length=255,blank=True,default='')
	cover_picture_thumb = models.ImageField(upload_to='content/categories/thumbs',max_length=100)
	title = models.CharField (max_length = 50)
	subtitle = models.CharField (max_length = 50)
	title_section_featured = models.CharField (max_length = 50)
	cities = models.ManyToManyField(City)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(Category,self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("detail_category",kwargs={"slug":self.slug})
