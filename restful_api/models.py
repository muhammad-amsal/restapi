#from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Portable_Object(models.Model):
	f_name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	date = models.DateField()

	def __str__(self):
		return self.f_name