#!/usr/bin/env python
# Python script for uploading a file to a Restful server
import requests

url_upload_form = 'http://localhost:1234/api/upload_form/'
url_upload_serializers = 'http://localhost:1234/api/upload_serializers/'

input = open('test.json', 'r')
data = input.read();
files = {'docfile': ('test.json', data)}
r=requests.post(url_upload_form, data={'title':'file_upload_form'}, files=files)
#r=requests.post(url_upload_serializers, data={'title':'file_upload_serializers'}, files=files