# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Image,Comment
from django.contrib import admin

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
	list_display = ['id', 'caption', 'image', 'slug', 'created']
	list_filter = ['created']

admin.site.register(Image, ImageAdmin)
admin.site.register(Comment)
