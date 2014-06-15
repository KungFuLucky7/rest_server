from django.forms import widgets
from rest_framework import serializers
from multipart_form_images.models import Image

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = ('image', 'title')
   

