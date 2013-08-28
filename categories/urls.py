from django.conf.urls import patterns, url, include
from . import views
from django.views.generic import DetailView
from categories.models import Category

urlpatterns = patterns('',
	url(r'^photographers/',include('freelancers.photographers.urls')), 
    url(r'^djs/',include('freelancers.djs.urls')),
    url(r'^tutors/',include('freelancers.tutors.urls')),      
    url(r'^(?P<slug>[\w-]+)/', DetailView.as_view(model = Category), name="detail_category"),
)