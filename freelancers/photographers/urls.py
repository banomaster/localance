from django.conf.urls import patterns, include, url
from . import views
from reviews.views import ReviewCreatePhotographer

urlpatterns = patterns('',
	  url(r'^add/$', views.PhotographerCreate.as_view(),name="add_photographer"),
      url(r'^(?P<slug>[\w-]+)/edit/$', views.PhotographerUpdate.as_view(), name="edit_photographer"),#
      url(r'^(?P<slug>[\w-]+)/delete/$', views.PhotographerDelete.as_view(), name="delete_photographer"),#
      url(r'^(?P<slug>[\w-]+)/reviews/add/$', ReviewCreatePhotographer.as_view(),name= "review_create_photographer"),
      url(r'^(?P<slug>[\w-]+)/inquiries/', include('inquiries.inquiries_photographers.urls')),
      url(r'^(?P<slug>[\w-]+)/$', views.PhotographerDetail.as_view(), name="detail_photographer"),#
      url(r'^$',views.PhotographerList.as_view(),name="list_photographers"),
)