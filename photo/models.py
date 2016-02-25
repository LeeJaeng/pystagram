# coding: utf-8

from __future__ import unicode_literals

from django.db import models


class Photo(models.Model):
	image_file = models.ImageField(upload_to='static_files/uploaded/original/%Y/%m/%d')
	filtered_image_file = models.ImageField(upload_to='static_files/uploaded/filtered/%Y/%m/%d')
	description = models.TextField(max_length=500, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
