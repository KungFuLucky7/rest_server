from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from multipart_form_images.models import Image
from multipart_form_images.serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser

@api_view(['GET','POST'])
def upload_form_images(request):
	if request.method == 'POST':
		instance = Image(image=request.FILES['image'], title=request.DATA['title'])
		instance.save()
		return Response('uploaded')
		
	elif request.method == 'GET':
		images = Image.objects.all()
		serializer = ImageSerializer(images)
		return Response(serializer.data)

@api_view(['POST','GET'])
def upload_serializers_images(request):
	if request.method == 'POST':
		serializer = ImageSerializer(data=request.DATA, files=request.FILES)
		if serializer.is_valid():
			serializer.save()
			return Response(data=request.DATA, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			
	elif request.method == 'GET':
		images = Image.objects.all()
		serializer = ImageSerializer(images)
		return Response(serializer.data)