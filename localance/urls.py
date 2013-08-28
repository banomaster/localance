from categories.views import CategoriesInCityList
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views as views
from accounts import views as accounts_views
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$',views.HomepageView.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('userena.urls')),
    url(r'^cph/$',CategoriesInCityList.as_view(), name = 'list_category'),
    url(r'^cph/',include('categories.urls')),
    url(r'', include('social_auth.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#import settings

# Serve media files only in development
#if settings.DEBUG:
#    urlpatterns += patterns('',
#        url(r'mugshots/(?P<path>.*)$', 'django.views.static.serve', {
#            'document_root': settings.MEDIA_ROOT_MUGSHOTS,
#        }),
#   )
#else:
#    print "no server is configured to serve media files. Do it now."