from django.db import models
from freelancers.tutors.models import ListTutorSkills
from inquiries.models import Inquiry

class InquiryTutor(Inquiry):
	subjects = models.ManyToManyField(ListTutorSkills)
	date = models.DateField(blank = True, null = True)
	estimated_budget = models.IntegerField(blank = True, null = True)