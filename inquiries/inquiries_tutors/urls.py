from django.conf.urls import patterns, url
from inquiries.inquiries_tutors.views import InquiryTutorCreate

urlpatterns = patterns('',
	  url(r'^add/$', InquiryTutorCreate.as_view(),name="post_inquiry"),
)