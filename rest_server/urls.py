from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rest_server.views.home', name='home'),
    # url(r'^rest_server/', include('rest_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include('multipart_form_data.urls')),
    url(r'^api/', include('multipart_form_images.urls')),
	url(r'^$', RedirectView.as_view(url='api/upload_form/', permanent=False)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))