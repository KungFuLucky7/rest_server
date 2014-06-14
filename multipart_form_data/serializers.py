from django.forms import widgets
from rest_framework import serializers
from multipart_form_data.models import File

class FileSerializer(serializers.ModelSerializer):
	class Meta:
		model = File
		fields = ('docfile', 'title')
   

