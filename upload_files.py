#!/usr/bin/env python
# Python script for uploading a file to a Restful server
import requests

# Upload a data file
url_upload_form = 'http://localhost:1234/api/upload_form/'
url_upload_serializers = 'http://localhost:1234/api/upload_serializers/'
input = open('test.json', 'r')
data = input.read();
files = {'docfile': ('test2.json', data)}
# r=requests.post(url_upload_form, data={'title':'file_upload_form'}, files=files)
#r=requests.post(url_upload_serializers, data={'title':'file_upload_serializers'}, files=files)

# Read the list of data files on server
r=requests.get(url_upload_serializers)
print r.content

# Upload an image
url_upload_form = 'http://localhost:1234/api/upload_form_images/'
url_upload_serializers = 'http://localhost:1234/api/upload_serializers_images/'
input = open('sample.jpg', 'r')
data = input.read();
images = {'image': ('sample.jpg', data)}
#r=requests.post(url_upload_form, data={'title':'file_upload_form_images'}, files=images)
#r=requests.post(url_upload_serializers, data={'title':'file_upload_serializers_images'}, files=images)

# Read the list of images on server
r=requests.get(url_upload_serializers)
print r.content

