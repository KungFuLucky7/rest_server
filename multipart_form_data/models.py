from django.db import models

class File(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, default='default_value')
	docfile = models.FileField(upload_to='files/')