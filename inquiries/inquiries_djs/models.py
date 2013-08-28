from django.db import models
from inquiries.models import Inquiry

class ListDJOccasion(models.Model):
	occasion = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.occasion

class InquiryDJ(Inquiry):
	occasion = models.ForeignKey(ListDJOccasion)
	date = models.DateField(blank = True, null = True)
	estimated_budget = models.IntegerField(blank = True, null = True)


