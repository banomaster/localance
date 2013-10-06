from core.views import ProfileMixin
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.contenttypes.models import ContentType
from freelancers.tutors.models import Tutor
from freelancers.tutors.forms import TutorForm
from reviews.models import Review

class TutorActionMixin(object):

	@property
	def action(self):
		msg = "{0} is missing action".format(self.__class__)
		raise NotImplementedError(msg)

	def form_valid(self, form):
		msg = "Tutor {0}!".format(self.action)
		messages.info(self.request, msg)
		return super(TutorActionMixin, self).form_valid(form)
	
class TutorCreate(TutorActionMixin, CreateView):
    form_class = TutorForm
    model = Tutor
    action = "created"

    def form_valid(self, form):
        form.instance.name = self.request.user.get_profile()
        return super(TutorCreate, self).form_valid(form)

class TutorUpdate(TutorActionMixin, UpdateView):
    model = Tutor
    action = "updated"#

class TutorDelete(DeleteView):
    model = Tutor
    success_url = reverse_lazy('tutors-list')

class TutorDetail(ProfileMixin, DetailView):
    model = Tutor
    context_object_name = 'tutor'

    def get_context_data(self, **kwargs):
    	context = super(TutorDetail, self).get_context_data(**kwargs)
        tutor = Tutor.objects.get(slug = self.kwargs['slug'])
        context['reviews'] = Review.objects.filter(object_id=tutor.id, freelancer=ContentType.objects.get_for_model(tutor))
        return context

class TutorList(ListView):
	model = Tutor
	context_object_name = 'tutors'