from .models import Review
from .forms import ReviewForm
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from freelancers.djs.models import DJ
from freelancers.photographers.models import Photographer
from freelancers.tutors.models import Tutor
from freelancers.models import Freelancer


class ReviewCreatePhotographer(CreateView):
    form_class = ReviewForm
    model = Review

    def post(self,request,*args,**kwargs):
    	review_form = ReviewForm(request.POST)
    	review = review_form.save(commit = False)
        freelancer = Photographer.objects.get(slug = self.kwargs['slug'])
    	review.object_id = freelancer.id
        review.freelancer=ContentType.objects.get_for_model(freelancer)
        review.user = self.request.user.get_profile()
        review.save()
        return HttpResponseRedirect('.')

class ReviewCreateTutor(CreateView):
    form_class = ReviewForm
    model = Review

    def post(self,request,*args,**kwargs):
        review_form = ReviewForm(request.POST)
        review = review_form.save(commit = False)
        freelancer = Tutor.objects.get(slug = self.kwargs['slug'])
        review.object_id = freelancer.id
        review.freelancer=ContentType.objects.get_for_model(freelancer)
        review.user = self.request.user.get_profile()
        review.save()
        return HttpResponseRedirect('.')

class ReviewCreateDJ(CreateView):
    form_class = ReviewForm
    model = Review

    def post(self,request,*args,**kwargs):
        review_form = ReviewForm(request.POST)
        review = review_form.save(commit = False)
        freelancer = DJ.objects.get(slug = self.kwargs['slug'])
        review.object_id = freelancer.id
        review.freelancer=ContentType.objects.get_for_model(freelancer)
        review.user = self.request.user.get_profile()
        review.save()
        return HttpResponseRedirect('.')
