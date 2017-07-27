from django.db import models

# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=3000)
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
	imageTitle = models.ImageField(upload_to = 'posters')

	def __str__(self):
		return self.title

class Event(models.Model):
	location = models.CharField(max_length=100)
	vrijeme = models.DateTimeField('Date Published')
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

	def __str__(self):
		return self.location