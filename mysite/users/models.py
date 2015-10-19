from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length = 10)
	def __str__(self):
		return self.name
	
class Works(models.Model):
 	artist = models.ForeignKey(User)
 	title = models.CharField(max_length = 10)
 	time = models.DateTimeField('date published')
 	def __str__(self):
 		return self.artist.title