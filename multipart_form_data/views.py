from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from multipart_form_data.models import File
from multipart_form_data.serializers import FileSerializer
from rest_framework.parsers import MultiPartParser, FormParser

@api_view(['GET','POST'])
def upload_form(request):
	if request.method == 'POST':
		instance = File(docfile=request.FILES['docfile'], title=request.DATA['title'])
		instance.save()
		return Response('uploaded')
		
	elif request.method == 'GET':
		files = File.objects.all()
		serializer = FileSerializer(files)
		return Response(serializer.data)

@api_view(['POST','GET'])
def upload_serializers(request):
	if request.method == 'POST':
		serializer = FileSerializer(data=request.DATA, files=request.FILES)
		if serializer.is_valid():
			serializer.save()
			return Response(data=request.DATA, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			
	elif request.method == 'GET':
		files = File.objects.all()
		serializer = FileSerializer(files)
		return Response(serializer.data)