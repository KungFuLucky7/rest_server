from django.conf.urls import patterns, url

urlpatterns = patterns('multipart_form_images.views',
    url(r'^upload_form_images/$', 'upload_form_images'),
    url(r'^upload_serializers_images/$', 'upload_serializers_images'),
)