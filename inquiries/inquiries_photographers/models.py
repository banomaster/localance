from django.db import models
from inquiries.models import Inquiry

class ListPhotographerOccasion(models.Model):
	occasion = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.occasion

class InquiryPhotographer(Inquiry):
	occasion = models.ForeignKey(ListPhotographerOccasion)
	date = models.DateField(blank = True, null = True)
	timeFrame = models.IntegerField(blank = True, null = True)
	estimatedBudget = models.IntegerField(blank = True, null = True)

