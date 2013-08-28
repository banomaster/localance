from django.contrib.contenttypes.models import ContentType
from django.views.generic.edit import CreateView
from freelancers.djs.models import DJ
from inquiries.inquiries_djs.models import InquiryDJ
from inquiries.inquiries_djs.forms import InquiryDJForm
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from core.views import AjaxableResponseMixin


class InquiryDJCreate(AjaxableResponseMixin, CreateView):
	form_class = InquiryDJForm
	model = InquiryDJ
	template_name="inquiries/inquiry_form.html"
	success_url = "."

	def form_valid(self, form):
		form.instance.user = self.request.user.get_profile()
		freelancer = DJ.objects.get(slug = self.kwargs['slug'])
		form.instance.object_id = freelancer.id
		form.instance.freelancer = ContentType.objects.get_for_model(freelancer)
		return super(InquiryDJCreate, self).form_valid(form)
# Create your views here.
