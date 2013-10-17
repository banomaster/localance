from core.views import ProfileMixin
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from freelancers.photographers.models import Photographer
from freelancers.photographers.forms import PhotographerForm
from reviews.models import Review

class PhotographerActionMixin(object):#

	@property
	def action(self):
		msg = "{0} is missing action".format(self.__class__)
		raise NotImplementedError(msg)

	def form_valid(self, form):
		msg = "Photographer {0}!".format(self.action)
		messages.info(self.request, msg)
		return super(PhotographerActionMixin, self).form_valid(form)
	
class PhotographerCreate(PhotographerActionMixin, ProfileMixin, CreateView):#
    form_class = PhotographerForm
    model = Photographer
    action = "created"#

    def form_valid(self, form):
        form.instance.name = self.request.user.get_profile()
        return super(PhotographerCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PhotographerCreate, self).get_context_data(**kwargs)
        photographers = Photographer.objects.all()
        l = []#photographers users
        for photographer in photographers:
            l.append(photographer.name.user.id)
        context['photographers'] = l
        return context

class PhotographerUpdate(PhotographerActionMixin, UpdateView):#
    model = Photographer
    action = "updated"#

class PhotographerDelete(DeleteView):
    model = Photographer
    success_url = reverse_lazy('photographers-list')

class PhotographerDetail(ProfileMixin, DetailView):
    model = Photographer
    context_object_name = 'photographer'

    def get_context_data(self, **kwargs):
     	context = super(PhotographerDetail, self).get_context_data(**kwargs)
        photographer = Photographer.objects.get(slug = self.kwargs['slug'])
        context['reviews'] = Review.objects.filter(object_id=photographer.id, freelancer=ContentType.objects.get_for_model(photographer))
        return context

class PhotographerList(ListView):
	model = Photographer
	context_object_name = 'photographers'
