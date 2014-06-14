#!/usr/bin/env python
# encoding: utf-8
"""
admin.py
"""

from multipart_form_data.models import File
from django.contrib import admin

class FileAdmin(admin.ModelAdmin):
    list_display = ('created', 'docfile')

admin.site.register(File, FileAdmin)
