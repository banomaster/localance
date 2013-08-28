from django.conf.urls import patterns, url
from inquiries.inquiries_photographers.views import InquiryPhotographerCreate

urlpatterns = patterns('',
	  url(r'^add/$', InquiryPhotographerCreate.as_view(),name="post_inquiry"),
)