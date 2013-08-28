from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
	  url(r'^add/$', views.ReviewCreate.as_view(),name="create_review"),
)