from django.contrib.contenttypes.models import ContentType
from django.views.generic.edit import CreateView
from freelancers.tutors.models import Tutor
from inquiries.inquiries_tutors.models import InquiryTutor
from inquiries.inquiries_tutors.forms import InquiryTutorForm
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from core.views import AjaxableResponseMixin


class InquiryTutorCreate(AjaxableResponseMixin, CreateView):
	form_class = InquiryTutorForm
	model = InquiryTutor
	template_name="inquiries/inquiry_form.html"
	success_url = "."

	def form_valid(self, form):
		form.instance.user = self.request.user.get_profile()
		freelancer = Tutor.objects.get(slug = self.kwargs['slug'])
		form.instance.object_id = freelancer.id
		form.instance.freelancer = ContentType.objects.get_for_model(freelancer)
		return super(InquiryTutorCreate, self).form_valid(form)
# Create your views here.
