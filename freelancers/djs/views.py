from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.contenttypes.models import ContentType
from freelancers.djs.models import DJ
from freelancers.djs.forms import DJForm
from reviews.models import Review

class DJActionMixin(object):

	@property
	def action(self):
		msg = "{0} is missing action".format(self.__class__)
		raise NotImplementedError(msg)

	def form_valid(self, form):
		msg = "DJ {0}!".format(self.action)
		messages.info(self.request, msg)
		return super(DJActionMixin, self).form_valid(form)
	
class DJCreate(DJActionMixin, CreateView):
    form_class = DJForm
    model = DJ
    action = "created"

class DJUpdate(DJActionMixin, UpdateView):
    model = DJ
    action = "updated"#

class DJDelete(DeleteView):
    model = DJ
    success_url = reverse_lazy('djs-list')

class DJDetail(DetailView):
    model = DJ 
    context_object_name = 'dj'

    def get_context_data(self, **kwargs):
     	context = super(DJDetail, self).get_context_data(**kwargs)
     	if self.request.user.is_authenticated():
     		context['profile'] = self.request.user.get_profile()
        dj = DJ.objects.get(slug = self.kwargs['slug'])
        context['reviews'] = Review.objects.filter(object_id=dj.id, freelancer=ContentType.objects.get_for_model(dj))
        return context

class DJList(ListView):
	model = DJ
	context_object_name = 'djs'