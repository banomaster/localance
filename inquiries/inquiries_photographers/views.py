from django.contrib.contenttypes.models import ContentType
from django.views.generic.edit import CreateView
from freelancers.photographers.models import Photographer
from inquiries.inquiries_photographers.models import InquiryPhotographer
from inquiries.inquiries_photographers.forms import InquiryPhotographerForm
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from core.views import AjaxableResponseMixin


class InquiryPhotographerCreate(AjaxableResponseMixin, CreateView):
	form_class = InquiryPhotographerForm
	model = InquiryPhotographer
	template_name="inquiries/inquiry_form.html"
	success_url = "."

	def form_valid(self, form):
		form.instance.user = self.request.user.get_profile()
		freelancer = Photographer.objects.get(slug = self.kwargs['slug'])
		form.instance.object_id = freelancer.id
		form.instance.freelancer = ContentType.objects.get_for_model(freelancer)
		return super(InquiryPhotographerCreate, self).form_valid(form)
