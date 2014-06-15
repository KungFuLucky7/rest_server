#!/usr/bin/env python
# encoding: utf-8
"""
admin.py
"""

from multipart_form_images.models import Image
from django.contrib import admin

class ImageAdmin(admin.ModelAdmin):
    list_display = ('created', 'image')

admin.site.register(Image, ImageAdmin)
