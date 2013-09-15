from django.http import HttpResponse
from django.views.generic.base import RedirectView
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
import json

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response# Create your views here.

class SignOut(RedirectView):

    permanent = False
    query_string = True
 
    def get_redirect_url(self):
        logout(self.request)
        return reverse('home')

class ProfileMixin(object):

   def get_context_data(self, **kwargs):
       context = super(ProfileMixin, self).get_context_data(**kwargs)
       if self.request.user.is_authenticated():
           context['profile'] = self.request.user.get_profile()
       return context
