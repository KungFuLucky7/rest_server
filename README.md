rest_server
======================================

RESTful External Archive Server for archiving data uploaded by the Field Observation Server


Reference
--------------
Andrew Smolik, multipart-form-data_django_rest_framework_tutorial, (2012), GitHub repository, https://github.com/ansother/multipart-form-data_django_rest_framework_tutorial


Uploading files
---------------

This files provides commands to upload files to the django-rest-framework api. 

1.	Open a python interpreter:

	``$ python``

2.	Import requests in python interpreter:

	``$import requests``
	
3. Swap out the YOUR_URL in the url variables with your root url:

	``$url_upload_form = 'YOUR_URL/api/upload_form/'``

	``$url_upload_serializers = 'YOUR_URL/api/upload_serializers/'``
	
4. Paste url variables into python interpreter:

5. Create a file to upload:

	``$files = {'docfile': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}``
	
6. Upload a file with a form:

	``$r=requests.post(url_upload_form, data={'title':'file_upload_form'}, files=files)``
	
7. Upload a file with django-rest-framework serializer:

	``$r=requests.post(url_upload_serializers, data={'title':'file_upload_serializers'}, files=files)``

8. To view uploaded data in the django-rest-framework view go to:

	``$YOUR_URL/api/upload_form/``
	
	or 
	
	``$YOUR_URL/api/upload_serializers/``


Uploading images
---------------

This files provides commands to upload images to the django-rest-framework api. 

1.	Open a python interpreter:

	``$ python``

2.	Import requests in python interpreter:

	``$import requests``
	
3. Swap out the YOUR_URL in the url variables with your root url:

	``$url_upload_form = 'YOUR_URL/api/upload_form_images/'``

	``$url_upload_serializers = 'YOUR_URL/api/upload_serializers_images/'``
	
4. Paste url variables into python interpreter:

5. Create an image to upload:

	``$images = {'image': ('image.jpg', image_data)}``
	
6. Upload a file with a form:

	``$r=requests.post(url_upload_form, data={'title':'file_upload_form_images'}, files=images)``
	
7. Upload a file with django-rest-framework serializer:

	``$r=requests.post(url_upload_serializers, data={'title':'file_upload_serializers_images'}, files=images)``

8. To view uploaded data in the django-rest-framework view go to:

	``$YOUR_URL/api/upload_form_images/``
	
	or 
	
	``$YOUR_URL/api/upload_serializers_images/``


Cloud version hosted on OpenShift
---------------
http://restservercloud-serveradmin.rhcloud.com/admin/



	

	

	



