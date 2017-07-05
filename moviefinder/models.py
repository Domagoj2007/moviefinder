from django.db import models

# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=3000)
	votes = models.IntegerField(default=0)

class Event(models.Model):
	location = models.CharField(max_length=100)
	vrijeme = models.DateTimeField('Date Published')
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)