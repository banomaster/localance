from django.conf.urls import patterns, url
from inquiries.inquiries_djs.views import InquiryDJCreate

urlpatterns = patterns('',
	  url(r'^add/$', InquiryDJCreate.as_view(),name="post_inquiry"),
)