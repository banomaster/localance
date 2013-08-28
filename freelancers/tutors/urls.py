from django.conf.urls import patterns, include, url
from . import views
from reviews.views import ReviewCreateTutor

urlpatterns = patterns('',
	  url(r'^add/$', views.TutorCreate.as_view(),name="add_tutor"),
      url(r'^(?P<slug>[\w-]+)/edit/$', views.TutorUpdate.as_view(), name="edit_tutor"),#
      url(r'^(?P<slug>[\w-]+)/delete/$', views.TutorDelete.as_view(), name="delete_tutor"),#
      url(r'^(?P<slug>[\w-]+)/reviews/add/$', ReviewCreateTutor.as_view(),name= "review_create_tutor"),
      url(r'^(?P<slug>[\w-]+)/inquiries/', include('inquiries.inquiries_tutors.urls')),
      url(r'^(?P<slug>[\w-]+)/$', views.TutorDetail.as_view(), name="detail_tutor"),#
      url(r'^$',views.TutorList.as_view(),name="list_tutors"),
)