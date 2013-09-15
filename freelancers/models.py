from django.db import models
from core.models import TimeStampedModel
from accounts.models import UserAccount	
from cities.models import City
from categories.models import Category
from django.template.defaultfilters import slugify


class Freelancer(TimeStampedModel):
	name = models.OneToOneField(UserAccount)
	nickname = models.CharField(max_length = 30, blank = True)
	slug = models.SlugField(max_length=255,blank=True,default='')
	about = models.TextField()
	tagline = models.TextField()
	cities = models.ManyToManyField(City)
	category = models.ForeignKey(Category, default = 3)
	personal_website = models.URLField(max_length = 40, blank = True)
	available = models.BooleanField(default = False)
	twitter_profile = models.URLField(max_length = 40, blank = True)
	linkedin_profile = models.URLField(max_length = 50, blank = True)
	featured_in_category = models.BooleanField(default = False)

	class Meta:
		abstract = True

	def __unicode__(self):
		return self.nickname 

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(Freelancer,self).save(*args, **kwargs)
