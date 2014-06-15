from django.db import models

class Image(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, default='default_value')
	image = models.FileField(upload_to='images/')