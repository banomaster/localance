from django.conf.urls import patterns, include, url
from . import views
from reviews.views import ReviewCreateDJ

urlpatterns = patterns('',
	  url(r'^add/$', views.DJCreate.as_view(),name="add_dj"),
      url(r'^(?P<slug>[\w-]+)/edit/$', views.DJUpdate.as_view(), name="edit_dj"),#
      url(r'^(?P<slug>[\w-]+)/delete/$', views.DJDelete.as_view(), name="delete_dj"),
	  url(r'^(?P<slug>[\w-]+)/reviews/add/$', ReviewCreateDJ.as_view(),name= "review_create_dj"),
	  url(r'^(?P<slug>[\w-]+)/inquiries/', include('inquiries.inquiries_djs.urls')),
      url(r'^(?P<slug>[\w-]+)/$', views.DJDetail.as_view(), name="detail_dj"),
      url(r'^$',views.DJList.as_view(),name="list_djs"),
)