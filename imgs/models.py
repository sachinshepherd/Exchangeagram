# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Image(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created')
	caption = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, blank=True)
	image = models.ImageField(upload_to='images/%Y/%m/%d')
	created = models.DateField(auto_now_add=True, db_index=True)
	users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

	class Meta:
		ordering = ('-created',)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.caption)
			super(Image, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('images:detail', args=[self.id, self.slug])


	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type

	def __str__(self):
		return 'image of user {}'.format(self.user.username)
	def __unicode__(self):
		return 'image of user {}'.format(self.user.username)


class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
	object_id = models.PositiveIntegerField(null=True)
	content_object = GenericForeignKey('content_type', 'object_id')

	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return str(self.user.username)
	def __unicode__(self):
		return str(self.user.username)
	class Meta:
		ordering = ['-timestamp']
