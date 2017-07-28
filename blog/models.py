# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.utils import timezone





# Create your models here.
# We define all objects called Models
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	#comment = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	#def comment_section(self):
		#self.comment = 

	def __str__(self):
		return self.title		


